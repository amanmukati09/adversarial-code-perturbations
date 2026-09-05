# Findings — Adversarial Perturbation Detection in AI-Generated Code

## Experiment 1: Detector Comparison (N=146 samples)

| Approach | Accuracy | Precision | Recall |
|----------|----------|-----------|--------|
| AST Features + XGBoost | 0.86 | 0.95 | 0.88 |
| CodeBERT Embeddings + LogReg | 0.79 | 0.86 | 0.91 |
| Ensemble (AST + Embeddings) | 0.80 | 0.87 | 0.90 |

**Key observation:** AST features outperform embeddings at this sample size.
Embeddings add noise, not signal, when data is limited.

## Experiment 2: Leave-One-Strategy-Out Analysis

| Perturbation Type | Detectable? | Notes |
|-------------------|-------------|-------|
| Comment planting | ✅ 100% | Structurally obvious (# comments) |
| Dead code insertion | ✅ 100% | `if False:` is a clear AST marker |
| Variable shadowing | ✅ 100% | Reassignment patterns catchable |
| Import aliasing | ❌ 4% | Single line, preserves structure |
| Boundary inversion | ❌ 0% | Single operator flip, no structural trace |

## Core Scientific Contribution

> **Static AST-based detection succeeds on structural perturbations
> (comments, dead code, shadowing) but fails completely on semantic
> perturbations (import aliasing, boundary inversion) that preserve
> syntactic structure while changing program behavior.**

This is a fundamental limitation of static analysis, not a bug.
AI-generated code can be adversarially attacked in ways that pass
through existing review pipelines undetected.

## Next Steps

1. Scale dataset to 500+ samples (automated generation + perturbation)
2. Test whether CodeBERT embeddings catch semantic perturbations better
   than AST features (with enough data)
3. Generalization study: train on one AI model, test on another
4. Detector evasion: can perturbed code be further modified to
   evade even the best detector?

## Reproducibility

- Environment: Python 3.14, WSL Ubuntu
- Dependencies: see requirements.txt
- Data: 146 samples (25 clean, 121 perturbed)
- Code: src/ directory, run scripts in order:
  1. `python src/perturber.py` — generates perturbed samples
  2. `python src/classifier.py` — AST-based detector
  3. `python src/embedding_detector.py` — embedding-based detector
  4. `python src/ensemble_detector.py` — combined approach
  5. `python src/per_strategy_analysis.py` — per-strategy breakdown
