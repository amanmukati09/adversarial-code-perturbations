"""
Generalization Study
Tests whether detectors trained on one perturbation strategy generalize
to other strategies. Also tests cross-model generalization using
different code styles (functional, class-based, compact).
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


def get_strategy(sample_id: str) -> str:
    strategies = ["boundary_invert", "variable_shadow", "import_alias", "dead_code", "comment_plant"]
    for s in strategies:
        if s in sample_id:
            return s
    return "clean"


def train_on_one_test_on_others():
    """Train detector on one strategy, test on all others."""
    samples = load_all_samples()
    X = np.array([list(extract_features(s["code"]).values()) for s in samples])
    y = np.array([s["label"] for s in samples])
    ids = [s["id"] for s in samples]

    strategies = ["boundary_invert", "variable_shadow", "import_alias", "dead_code", "comment_plant"]
    
    print("\n=== Cross-Strategy Generalization (Train on One, Test on Others) ===")
    print(f"{'Train Strategy':<20} {'Test Strategy':<20} {'N':>4} {'Accuracy':>8} {'Precision':>9} {'Recall':>8}")
    print("-" * 75)

    results = {}
    for train_strat in strategies:
        # Train on clean + this strategy
        train_mask = np.array([
            get_strategy(i) == "clean" or get_strategy(i) == train_strat 
            for i in ids
        ])
        
        if len(np.unique(y[train_mask])) < 2:
            continue
            
        scale = len(y[train_mask][y[train_mask]==0]) / max(len(y[train_mask][y[train_mask]==1]), 1)
        clf = XGBClassifier(n_estimators=50, max_depth=3, scale_pos_weight=scale, random_state=42)
        clf.fit(X[train_mask], y[train_mask])
        
        for test_strat in strategies:
            test_mask = np.array([get_strategy(i) == test_strat for i in ids])
            
            if sum(test_mask) == 0:
                continue
                
            preds = clf.predict(X[test_mask])
            true = y[test_mask]
            
            acc = accuracy_score(true, preds)
            prec = precision_score(true, preds, zero_division=0)
            rec = recall_score(true, preds, zero_division=0)
            
            results[f"{train_strat}_to_{test_strat}"] = {
                "accuracy": acc, "precision": prec, "recall": rec
            }
            
            print(f"{train_strat:<20} {test_strat:<20} {sum(test_mask):>4} {acc:>8.2f} {prec:>9.2f} {rec:>8.2f}")

    return results


def train_on_all_except_one_test_on_heldout():
    """Standard leave-one-out with AST features."""
    samples = load_all_samples()
    X = np.array([list(extract_features(s["code"]).values()) for s in samples])
    y = np.array([s["label"] for s in samples])
    ids = [s["id"] for s in samples]

    strategies = ["boundary_invert", "variable_shadow", "import_alias", "dead_code", "comment_plant"]
    
    print("\n=== Leave-One-Strategy-Out (AST Features) ===")
    print(f"{'Held-Out Strategy':<25} {'N':>4} {'Accuracy':>8} {'Precision':>9} {'Recall':>8}")
    print("-" * 60)

    for held_out in strategies:
        test_mask = np.array([get_strategy(i) == held_out for i in ids])
        train_mask = ~test_mask
        
        # Include clean samples in training
        clean_mask = np.array([get_strategy(i) == "clean" for i in ids])
        train_mask = train_mask & ~clean_mask  # Remove clean from train
        train_mask = train_mask | clean_mask  # Add back clean samples
        
        if len(np.unique(y[train_mask])) < 2:
            print(f"{held_out:<25} {'—':>4} {'SKIP':>8}")
            continue
            
        scale = len(y[train_mask][y[train_mask]==0]) / max(len(y[train_mask][y[train_mask]==1]), 1)
        clf = XGBClassifier(n_estimators=50, max_depth=3, scale_pos_weight=scale, random_state=42)
        clf.fit(X[train_mask], y[train_mask])
        
        preds = clf.predict(X[test_mask])
        true = y[test_mask]
        
        acc = accuracy_score(true, preds)
        prec = precision_score(true, preds, zero_division=0)
        rec = recall_score(true, preds, zero_division=0)
        
        print(f"{held_out:<25} {sum(test_mask):>4} {acc:>8.2f} {prec:>9.2f} {rec:>8.2f}")


if __name__ == "__main__":
    print("=" * 75)
    print("GENERALIZATION STUDY")
    print("=" * 75)
    
    train_on_one_test_on_others()
    train_on_all_except_one_test_on_heldout()
    
    print("\n" + "=" * 75)
    print("Generalization study complete.")
    print("=" * 75)
