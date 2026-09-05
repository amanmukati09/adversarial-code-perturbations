"""
Statistical Significance Tests
McNemar's test for paired classifier comparison.
Evaluates whether AST-based detector significantly outperforms embedding-based.
"""

import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from transformers import AutoTokenizer, AutoModel
import torch
from statsmodels.stats.contingency_tables import mcnemar

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


def get_predictions(clf, X, y):
    """Get cross-validated predictions."""
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    return cross_val_predict(clf, X, y, cv=cv, method="predict")


if __name__ == "__main__":
    print("Loading data...")
    samples = load_all_samples()
    
    print("Building AST features...")
    X_ast = np.array([list(extract_features(s["code"]).values()) for s in samples])
    y = np.array([s["label"] for s in samples])

    print("Building CodeBERT embeddings...")
    embedder = CodeEmbedder()
    X_emb = np.array([embedder.embed(s["code"]) for s in samples])

    # Track A: AST + XGBoost
    scale = len(y[y==0]) / len(y[y==1]) if len(y[y==1]) > 0 else 1
    ast_clf = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", XGBClassifier(n_estimators=100, max_depth=4, scale_pos_weight=scale, random_state=42))
    ])

    # Track B: Embeddings + LogReg
    emb_clf = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced"))
    ])

    print("\nGetting cross-validated predictions...")
    ast_preds = get_predictions(ast_clf, X_ast, y)
    emb_preds = get_predictions(emb_clf, X_emb, y)

    # Build contingency table
    # Table: [ [both correct, AST correct & EMB wrong], 
    #          [AST wrong & EMB correct, both wrong] ]
    both_correct = np.sum((ast_preds == y) & (emb_preds == y))
    ast_only = np.sum((ast_preds == y) & (emb_preds != y))
    emb_only = np.sum((ast_preds != y) & (emb_preds == y))
    both_wrong = np.sum((ast_preds != y) & (emb_preds != y))

    table = np.array([[both_correct, ast_only],
                      [emb_only, both_wrong]])

    print("\n=== Contingency Table ===")
    print(f"Both correct: {both_correct}")
    print(f"AST only correct: {ast_only}")
    print(f"Embedding only correct: {emb_only}")
    print(f"Both wrong: {both_wrong}")

    # McNemar's test
    result = mcnemar(table, exact=True, correction=True)
    print(f"\n=== McNemar's Test ===")
    print(f"Statistic: {result.statistic:.4f}")
    print(f"p-value: {result.pvalue:.4f}")

    alpha = 0.05
    if result.pvalue < alpha:
        print(f"\n✅ Statistically significant (p < {alpha})")
        if ast_only > emb_only:
            print("   AST-based detector significantly outperforms embedding-based.")
        else:
            print("   Embedding-based detector significantly outperforms AST-based.")
    else:
        print(f"\n❌ Not statistically significant (p >= {alpha})")
        print("   Cannot reject null hypothesis that detectors perform equally.")

    # Also compare accuracy
    ast_acc = np.mean(ast_preds == y)
    emb_acc = np.mean(emb_preds == y)
    print(f"\n=== Accuracy Comparison ===")
    print(f"AST: {ast_acc:.4f}")
    print(f"CodeBERT: {emb_acc:.4f}")
    print(f"Difference: {abs(ast_acc - emb_acc):.4f}")

    print("\nDone.")
