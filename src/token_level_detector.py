"""
Token-Level CodeBERT Detector
Uses CLS token and max-pooled token representations to preserve
single-token changes that mean-pooling washes out.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold, cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from transformers import AutoTokenizer, AutoModel
import torch

from dataset_loader import load_all_samples

MODEL_NAME = "microsoft/codebert-base"


class TokenLevelEmbedder:
    """Embeds code using CLS token + max pooling to preserve token-level signals."""

    def __init__(self, model_name=MODEL_NAME):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.model.eval()

    def embed(self, code: str) -> np.ndarray:
        inputs = self.tokenizer(
            code, return_tensors="pt", truncation=True, max_length=512, padding=True
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Get last hidden state: [batch_size, seq_len, hidden_dim]
        last_hidden = outputs.last_hidden_state.squeeze(0)  # [seq_len, 768]
        
        # CLS token representation (first token)
        cls_embedding = last_hidden[0].numpy()  # [768]
        
        # Max pooling over all tokens (preserves strongest signals)
        max_embedding = last_hidden.max(dim=0).values.numpy()  # [768]
        
        # Mean pooling for comparison
        mean_embedding = last_hidden.mean(dim=0).numpy()  # [768]
        
        # Concatenate all three representations
        return np.concatenate([cls_embedding, max_embedding, mean_embedding])  # [2304]


def get_strategy(sample_id: str) -> str:
    strategies = ["boundary_invert", "variable_shadow", "import_alias", "dead_code", "comment_plant"]
    for s in strategies:
        if s in sample_id:
            return s
    return "clean"


if __name__ == "__main__":
    print("Loading samples...")
    samples = load_all_samples()
    
    print("Building token-level embeddings...")
    embedder = TokenLevelEmbedder()
    X = np.array([embedder.embed(s["code"]) for s in samples])
    y = np.array([s["label"] for s in samples])
    ids = [s["id"] for s in samples]

    print(f"Embedding shape: {X.shape}")  # Should be (550, 2304)

    # Overall detection
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=2000, random_state=42, class_weight="balanced"))
    ])

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    print("\n=== Token-Level CodeBERT (CLS + Max + Mean) ===")
    for metric_name, scorer in [
        ("Accuracy", "accuracy"),
        ("Precision", "precision"),
        ("Recall", "recall"),
    ]:
        scores = cross_val_score(pipe, X, y, cv=cv, scoring=scorer)
        print(f"{metric_name}: {scores.mean():.2f} (+/- {scores.std():.2f})")

    # Per-strategy analysis
    print("\n=== Per-Strategy Detection (Token-Level) ===")
    print(f"{'Strategy':<25} {'N':>4} {'Recall':>8}")
    
    for strategy in ["boundary_invert", "import_alias", "variable_shadow", "dead_code", "comment_plant"]:
        # Train on all except this strategy
        test_mask = np.array([get_strategy(i) == strategy for i in ids])
        train_mask = np.array([get_strategy(i) != strategy and get_strategy(i) != "clean" for i in ids])
        
        # Add clean samples to training
        clean_mask = np.array([get_strategy(i) == "clean" for i in ids])
        train_mask = train_mask | clean_mask
        
        if len(np.unique(y[train_mask])) < 2:
            print(f"{strategy:<25} {'—':>4} {'SKIP (no train data)':>8}")
            continue
        
        clf = LogisticRegression(max_iter=2000, random_state=42, class_weight="balanced")
        clf.fit(X[train_mask], y[train_mask])
        
        preds = clf.predict(X[test_mask])
        true = y[test_mask]
        
        if len(true) > 0:
            recall = np.mean(preds == true)
            n = len(true)
            print(f"{strategy:<25} {n:>4} {recall:>8.2f}")

    print("\nDone.")
