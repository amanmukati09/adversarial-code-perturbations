"""
Per-Strategy Detection Analysis
Measures how well each detector catches each perturbation type.
"""

import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import StratifiedKFold, cross_val_score
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


def get_strategy_from_id(sample_id: str) -> str:
    """Extract strategy name from sample ID."""
    strategies = ["boundary_invert", "variable_shadow", "import_alias", "dead_code", "comment_plant"]
    for s in strategies:
        if s in sample_id:
            return s
    return "original_or_handmade"


if __name__ == "__main__":
    print("Loading samples...")
    samples = load_all_samples()

    # Group by strategy
    strategies = {}
    for s in samples:
        strat = get_strategy_from_id(s["id"])
        if strat not in strategies:
            strategies[strat] = []
        strategies[strat].append(s)

    print(f"\nStrategy breakdown:")
    for strat, items in sorted(strategies.items()):
        clean = sum(1 for i in items if i["label"] == 0)
        pert = sum(1 for i in items if i["label"] == 1)
        print(f"  {strat}: {len(items)} total ({clean} clean, {pert} perturbed)")

    # Train AST-based detector and test per strategy
    print("\nLoading embedder...")
    embedder = CodeEmbedder()

    print("Building features...")
    X_ast = []
    X_emb = []
    y = []
    ids = []

    for s in samples:
        feats = extract_features(s["code"])
        X_ast.append(list(feats.values()))
        X_emb.append(embedder.embed(s["code"]))
        y.append(s["label"])
        ids.append(s["id"])

    X_ast = np.array(X_ast)
    X_emb = np.array(X_emb)
    y = np.array(y)

    # Use leave-one-strategy-out: train on all strategies except one, test on held-out
    print("\n--- Leave-One-Strategy-Out Results (AST + XGBoost) ---")
    print(f"{'Held-out strategy':<25} {'N':>4} {'Accuracy':>8} {'Precision':>9} {'Recall':>8}")

    for held_out in sorted(strategies.keys()):
        
        
        # Skip if held-out has no clean samples OR train has no perturbed
        train_mask = np.array([get_strategy_from_id(i) != held_out for i in ids])
        if len(np.unique(y[train_mask])) < 2:
            print(f"  Skipping {held_out} (train set has only one class)")
            continue
        
        test_mask = np.array([get_strategy_from_id(i) == held_out for i in ids])

        if sum(test_mask) == 0:
            continue

        # Train on all but held-out
        scale = len(y[train_mask][y[train_mask]==0]) / max(len(y[train_mask][y[train_mask]==1]), 1)
        clf = XGBClassifier(n_estimators=50, max_depth=3, scale_pos_weight=scale, random_state=42)
        clf.fit(X_ast[train_mask], y[train_mask])

        # Predict on held-out
        preds = clf.predict(X_ast[test_mask])
        true = y[test_mask]

        acc = accuracy_score(true, preds)
        prec = precision_score(true, preds, zero_division=0)
        rec = recall_score(true, preds, zero_division=0)

        print(f"{held_out:<25} {sum(test_mask):>4} {acc:>8.2f} {prec:>9.2f} {rec:>8.2f}")

    print("\nDone.")
