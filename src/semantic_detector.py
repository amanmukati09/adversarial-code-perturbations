"""
Semantic Detector
Focuses specifically on detecting semantically-perturbed code
(import aliasing, boundary inversion) using embeddings.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from transformers import AutoTokenizer, AutoModel
import torch

from dataset_loader import load_all_samples

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


def get_strategy(sample_id: str) -> str:
    strategies = ["boundary_invert", "variable_shadow", "import_alias", "dead_code", "comment_plant"]
    for s in strategies:
        if s in sample_id:
            return s
    return "clean"


if __name__ == "__main__":
    samples = load_all_samples()
    print(f"Total samples: {len(samples)}")

    # Focus only on clean + hard semantic perturbations
    hard_strategies = {"boundary_invert", "import_alias"}
    focus_samples = [s for s in samples if get_strategy(s["id"]) in hard_strategies or s["label"] == 0]

    print(f"Focus samples (clean + semantic pert): {len(focus_samples)}")

    embedder = CodeEmbedder()
    X = np.array([embedder.embed(s["code"]) for s in focus_samples])
    y = np.array([s["label"] for s in focus_samples])

    print(f"X shape: {X.shape}")
    print(f"Class balance: {dict(zip(*np.unique(y, return_counts=True)))}")

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced"))
    ])

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    print("\n--- Semantic Detection (CodeBERT embeddings) ---")
    for metric_name, scorer in [
        ("Accuracy", "accuracy"),
        ("Precision", "precision"),
        ("Recall", "recall"),
    ]:
        scores = cross_val_score(pipe, X, y, cv=cv, scoring=scorer)
        print(f"{metric_name}: {scores.mean():.2f} (+/- {scores.std():.2f})")

    print("\nDone.")
