"""
Embedding-Based Detector (Track B)
Uses a pre-trained code embedding model to detect perturbed code.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from transformers import AutoTokenizer, AutoModel
import torch

from dataset_loader import load_all_samples

# Use a small, CPU-friendly code embedding model
MODEL_NAME = "microsoft/codebert-base"


class CodeEmbedder:
    """Embeds code snippets using CodeBERT."""

    def __init__(self, model_name=MODEL_NAME):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.model.eval()

    def embed(self, code: str) -> np.ndarray:
        """Return a fixed-size vector for a code snippet."""
        inputs = self.tokenizer(
            code, return_tensors="pt", truncation=True, max_length=512, padding=True
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
        # Mean pooling over token dimension
        embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
        return embedding


if __name__ == "__main__":
    print("Loading samples...")
    samples = load_all_samples()
    X_codes = [s["code"] for s in samples]
    y = np.array([s["label"] for s in samples])

    print("Loading CodeBERT... (first run downloads ~500MB)")
    embedder = CodeEmbedder()

    print("Embedding samples...")
    X_emb = np.array([embedder.embed(code) for code in X_codes])
    print(f"Embedding shape: {X_emb.shape}")

    # Train logistic regression on embeddings
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, random_state=42))
    ])

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    print("\n--- Cross-Validation (Embedding-based) ---")
    for metric_name, scorer in [
        ("Accuracy", "accuracy"),
        ("Precision", "precision"),
        ("Recall", "recall"),
    ]:
        scores = cross_val_score(pipe, X_emb, y, cv=cv, scoring=scorer)
        print(f"{metric_name}: {scores.mean():.2f} (+/- {scores.std():.2f})")

    print("\nDone.")
