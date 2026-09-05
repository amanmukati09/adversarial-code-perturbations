# Adversarial Code Perturbations

**Detecting Adversarial Perturbations in AI-Generated Code: A Three-Tier Detectability Hierarchy**

[![Python 3.14](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

AI code generation systems are increasingly deployed in production, yet the security implications of adversarially perturbed AI-generated code remain critically underexplored. This project systematically studies **five perturbation strategies** that an adversary could use to introduce subtle bugs or vulnerabilities into AI-generated Python functions while preserving syntactic plausibility.

Using a dataset of **550 samples** (100 clean, 450 perturbed), we evaluate three detection approaches:

| Approach | Method | Accuracy | Precision | Recall |
|----------|--------|----------|-----------|--------|
| **Track A** | AST Features + XGBoost | **0.91** | **0.96** | 0.93 |
| **Track B** | Mean-Pooled CodeBERT + LogReg | 0.87 | 0.91 | **0.93** |
| **Track C** | Token-Level CodeBERT + LogReg | 0.88 | 0.92 | **0.93** |

## Key Finding: Three-Tier Detectability Hierarchy

Our central finding is a **three-tier detectability hierarchy**:

| Tier | Perturbation Type | Detectability | Recall |
|------|-------------------|---------------|--------|
| **1** | Comment planting, Dead code, Variable shadowing | Trivially detected | 1.00 |
| **2** | Import aliasing | Feature-specific | 0.07-0.17 |
| **3** | Boundary inversion | Invisible | 0.00 |

> **Scientific Contribution:** Static AST-based detection succeeds on structural perturbations but fails completely on semantic perturbations that preserve syntactic structure while changing program behavior. This is a fundamental limitation, not a sample size artifact.

## Statistical Validation

McNemar's test confirms AST features significantly outperform embeddings:

| Comparison | Statistic | p-value | Significant? |
|------------|-----------|---------|--------------|
| AST vs CodeBERT | 9.00 | 0.0201 | Yes (p < 0.05) |

## Cross-Strategy Generalization

Training on boundary inversion unexpectedly generalizes to other strategies (recall 0.38-1.00), while training on import aliasing produces narrowly specialized detectors (recall 0.00-0.46).

## Repository Structure

```
adversarial-code-perturbations/
├── data/
│   └── seed_samples/
│       ├── clean/          # 100 AI-generated Python functions
│       └── perturbed/      # 450 adversarially perturbed variants
├── src/
│   ├── config.py                  # Central configuration
│   ├── generator.py               # Seed prompt definitions
│   ├── generate_clean_batch.py    # Batch clean sample generator
│   ├── perturber.py               # 5 perturbation strategies
│   ├── dataset_loader.py          # Labeled data loading
│   ├── feature_extractor.py       # 17 AST features
│   ├── classifier.py              # Track A: AST + XGBoost
│   ├── embedding_detector.py      # Track B: Mean-pooled CodeBERT
│   ├── token_level_detector.py    # Track C: Token-level CodeBERT
│   ├── ensemble_detector.py       # Combined approach
│   ├── semantic_detector.py       # Focused semantic analysis
│   ├── per_strategy_analysis.py   # Leave-one-strategy-out
│   ├── generalization_study.py    # Cross-strategy generalization
│   ├── statistical_tests.py       # McNemar's significance test
│   └── generate_figures.py        # Publication-quality figures
├── paper/
│   ├── main.tex                   # Complete LaTeX paper (8 pages)
│   ├── findings.md                # Detailed experimental results
│   └── figures/                   # 3 publication-quality figures
├── arxiv_submission/              # Ready-to-submit package
│   ├── main.tex
│   └── figures/
├── hypothesis.md                  # Research questions
├── requirements.txt               # Dependencies
├── LICENSE                        # MIT License
└── README.md                      # This file
```

## Perturbation Strategies

| Strategy | Type | Description | Example |
|----------|------|-------------|---------|
| **Comment planting** | Structural | Insert commented-out malicious code | `# dangerous_call()` |
| **Dead code insertion** | Structural | Add `if False:` blocks with payloads | `if False: bypass()` |
| **Variable shadowing** | Structural | Reassign parameters to mask values | `result = copy(result)` |
| **Import aliasing** | Semantic | Alias unsafe imports deceptively | `from md5 import sha256` |
| **Boundary inversion** | Semantic | Flip comparison operators | `<` to `<=` |

## Quick Start

### Prerequisites

- Python 3.10+
- pip
- git

### Installation

```bash
git clone https://github.com/amanmukati09/adversarial-code-perturbations.git
cd adversarial-code-perturbations
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running Experiments

```bash
python src/perturber.py
python src/classifier.py
python src/embedding_detector.py
python src/token_level_detector.py
python src/per_strategy_analysis.py
python src/generalization_study.py
python src/statistical_tests.py
python src/generate_figures.py
```

## Compiling the Paper

```bash
cd paper
pdflatex main.tex
pdflatex main.tex
```

The compiled PDF is `main.pdf` (8 pages, 3 figures, 6 tables, statistical validation).

## Submission

The `arxiv_submission/` directory contains everything needed for arXiv or workshop submission:

- `main.tex` — the complete paper
- `figures/` — all figures in optimized PNG format

### Suggested Venues

| Venue | Deadline (typical) | Format |
|-------|-------------------|--------|
| NeurIPS Safe & Robust AI Workshop | June-July annually | 4-8 pages |
| USENIX WOOT | Varies | 6-12 pages |
| ACM CCS AI Security Workshop | Varies | 6-12 pages |
| ICML Workshop on Adversarial ML | Varies | 4-8 pages |

## Citation

```bibtex
@misc{mukati2026adversarial,
  author = {Mukati, Aman},
  title = {Detecting Adversarial Perturbations in AI-Generated Code: A Three-Tier Detectability Hierarchy},
  year = {2026},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.22349074},
  url = {https://doi.org/10.5281/zenodo.22349074}
}
```

## Future Work

- Multi-model generalization (train on Codex, test on DeepSeek)
- Execution-based detection (run code in sandbox, compare outputs)
- Attention-based CodeBERT (not just CLS/max/mean pooling)
- Adversarial training of detectors (improve robustness)
- Extend to JavaScript, TypeScript, and other languages
- Real-world vulnerability injection testing

## License

MIT License — see [LICENSE](LICENSE) for details.

## Contact

- **GitHub**: [@amanmukati09](https://github.com/amanmukati09)
- **Email**: amanmukati2002@gmail.com
- **Project**: [https://github.com/amanmukati09/adversarial-code-perturbations](https://github.com/amanmukati09/adversarial-code-perturbations)
