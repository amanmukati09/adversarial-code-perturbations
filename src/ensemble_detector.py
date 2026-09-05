"""
Ensemble Detector
Combines AST features + CodeBERT embeddings for robust detection.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from transformers import AutoTokenizer, AutoModel
import torch

from dataset_loader import load_all_samples
from feature_extractor import extract_features

MODEL_NAME = "microsoft/codebert-base"


class CodeEmbedder:
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
        return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()


def build_combined_features():
    """Combine AST features and embeddings for all samples."""
    samples = load_all_samples()
    embedder = CodeEmbedder()

    ast_features = []
    embeddings = []
    y = []

    for s in samples:
        code = s["code"]
        feats = extract_features(code)
        ast_features.append(list(feats.values()))
        embeddings.append(embedder.embed(code))
        y.append(s["label"])

    X_ast = np.array(ast_features)
    X_emb = np.array(embeddings)
    X_combined = np.hstack([X_ast, X_emb])
    y = np.array(y)

    return X_combined, y


if __name__ == "__main__":
    print("Building combined features...")
    X, y = build_combined_features()
    print(f"Combined shape: {X.shape}")

    # XGBoost on combined features
    scale = len(y[y==0]) / len(y[y==1]) if len(y[y==1]) > 0 else 1
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", XGBClassifier(
            n_estimators=100,
            max_depth=4,
            scale_pos_weight=scale,
            random_state=42
        ))
    ])

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    print("\n--- Cross-Validation (Ensemble) ---")
    for metric_name, scorer in [
        ("Accuracy", "accuracy"),
        ("Precision", "precision"),
        ("Recall", "recall"),
    ]:
        scores = cross_val_score(pipe, X, y, cv=cv, scoring=scorer)
        print(f"{metric_name}: {scores.mean():.2f} (+/- {scores.std():.2f})")

    print("\nDone.")
