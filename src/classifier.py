"""
Baseline Classifier
Trains XGBoost on AST + text features to detect perturbed code.
"""

import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
import sys
sys.path.append("src")

from dataset_loader import load_all_samples
from feature_extractor import extract_features



def build_dataset():
    """Load samples, extract features, return X, y, sample_ids."""
    from dataset_loader import load_all_samples
    samples = load_all_samples()
    X_list = []
    y_list = []
    ids = []

    for s in samples:
        code = s["code"]
        feats = extract_features(code)
        X_list.append(list(feats.values()))
        y_list.append(s["label"])
        ids.append(s["id"])

    feature_names = list(extract_features("def foo(): pass").keys())
    return np.array(X_list), np.array(y_list), ids, feature_names



if __name__ == "__main__":
    X, y, ids, feature_names = build_dataset()
    print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")
    print(f"Labels: {dict(zip(*np.unique(y, return_counts=True)))}")


    # Use scale_pos_weight to handle any remaining imbalance
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
    from sklearn.metrics import make_scorer, precision_score, recall_score

    print("\n--- Cross-Validation ---")
    for metric_name, scorer in [
        ("Accuracy", "accuracy"),
        ("Precision", make_scorer(precision_score)),
        ("Recall", make_scorer(recall_score)),
    ]:
        scores = cross_val_score(pipe, X, y, cv=cv, scoring=scorer)
        print(f"{metric_name}: {scores.mean():.2f} (+/- {scores.std():.2f})")





    # Train on full data and show feature importances
    pipe.fit(X, y)
    importances = pipe.named_steps["clf"].feature_importances_
    print("\nFeature importances:")
    for name, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1]):
        print(f"  {name}: {imp:.4f}")
