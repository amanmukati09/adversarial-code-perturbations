# Adversarial Code Perturbations

**Detecting Adversarial Perturbations in AI-Generated Code: A Study of Static and Embedding-Based Approaches**

[![Python 3.14](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

AI code generation systems are increasingly used to produce production software, yet the security implications of adversarially perturbed AI-generated code remain underexplored. This project systematically studies **five perturbation strategies** that an adversary could use to introduce subtle bugs or vulnerabilities into AI-generated Python functions while preserving syntactic plausibility.

Using a dataset of **550 samples** (100 clean, 450 perturbed), we evaluate two detection approaches:

| Approach | Method | Accuracy | Precision | Recall |
|----------|--------|----------|-----------|--------|
| **Track A** | AST Features + XGBoost | **0.91** | **0.96** | 0.93 |
| **Track B** | CodeBERT Embeddings + LogReg | 0.87 | 0.91 | **0.93** |
| **Ensemble** | Combined Features | 0.87 | 0.92 | 0.92 |

## Key Finding: Three-Tier Detectability Hierarchy

Our most significant finding emerges from leave-one-strategy-out evaluation:

| Perturbation Type | Detectability | Recall |
|-------------------|---------------|--------|
| Comment planting | ✅ Trivially detected | 1.00 |
| Dead code insertion | ✅ Trivially detected | 1.00 |
| Variable shadowing | ✅ Trivially detected | 1.00 |
| Import aliasing | ❌ Nearly invisible | 0.07 |
| Boundary inversion | ❌ Completely invisible | 0.00 |

> **Scientific Contribution:** Static AST-based detection succeeds on structural perturbations but fails completely on semantic perturbations that preserve syntactic structure while changing program behavior. This is a fundamental limitation, not a sample size artifact.

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
│   ├── embedding_detector.py      # Track B: CodeBERT + LogReg
│   ├── ensemble_detector.py       # Combined approach
│   ├── semantic_detector.py       # Focused semantic analysis
│   └── per_strategy_analysis.py   # Leave-one-strategy-out
├── paper/
│   ├── main.tex                   # Complete LaTeX paper
│   └── findings.md                # Detailed experimental results
├── hypothesis.md                  # Research questions
├── requirements.txt               # Dependencies
└── README.md                      # This file
```

## Perturbation Strategies

| Strategy | Type | Description | Example |
|----------|------|-------------|---------|
| **Comment planting** | Structural | Insert commented-out malicious code | `# import subprocess; subprocess.run(['rm', '-rf', '/'])` |
| **Dead code insertion** | Structural | Add `if False:` blocks with payloads | `if False: dangerous_call()` |
| **Variable shadowing** | Structural | Reassign parameters to mask original values | `result = [x for x in result]` |
| **Import aliasing** | Semantic | Alias unsafe imports with misleading names | `from hashlib import md5 as sha256` |
| **Boundary inversion** | Semantic | Flip comparison operators or boundaries | `<` → `<=`, `len-1` → `len` |

## Quick Start

### Prerequisites

- Python 3.10+
- pip
- git

### Installation

```bash
# Clone the repository
git clone https://github.com/amanmukati09/adversarial-code-perturbations.git
cd adversarial-code-perturbations

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Experiments

```bash
# 1. Generate clean samples (if starting from scratch)
python src/generate_clean_batch.py

# 2. Generate perturbed samples
python src/perturber.py

# 3. Run AST-based detector (Track A)
python src/classifier.py

# 4. Run embedding-based detector (Track B)
python src/embedding_detector.py

# 5. Run ensemble detector
python src/ensemble_detector.py

# 6. Run per-strategy analysis
python src/per_strategy_analysis.py
```

## Results

All experimental results are documented in [`paper/findings.md`](paper/findings.md).

The complete paper is available in [`paper/main.tex`](paper/main.tex) and can be compiled with:

```bash
cd paper
pdflatex main.tex
pdflatex main.tex
```

## Key Insights

1. **AST features dominate at all scales** — simple structural features outperform CodeBERT embeddings for our perturbation types.

2. **Embeddings improve with data** — CodeBERT accuracy improved from 0.79 (N=146) to 0.87 (N=550), but never surpassed AST features.

3. **Ensemble provides no benefit** — combining AST features with embeddings adds variance without improving detection.

4. **Semantic perturbations are the real threat** — import aliasing and boundary inversion evade detection entirely, even with embeddings.

## Limitations

- **Python-only**: Results may not transfer to other programming languages.
- **Synthetic perturbations**: Real-world attackers may use more sophisticated strategies.
- **Mean-pooling**: Token-level analysis may capture semantic changes better.
- **No execution-based analysis**: Static methods cannot observe behavioral differences.

## Future Work

- [ ] Test on code from multiple LLMs (Codex, DeepSeek, Gemini) for generalization study
- [ ] Implement token-level CodeBERT analysis instead of mean-pooling
- [ ] Add execution-based detection (run code in sandbox, compare outputs)
- [ ] Explore adversarial training of detectors
- [ ] Extend to JavaScript, TypeScript, and other languages
- [ ] Run statistical significance tests (McNemar's test)
- [ ] Submit to NeurIPS Safe & Robust AI Workshop or USENIX WOOT

## Citation

If you use this code or findings in your research, please cite:

```bibtex
@misc{adversarial-code-perturbations,
  author = {Aman Mukati},
  title = {Detecting Adversarial Perturbations in AI-Generated Code},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/amanmukati09/adversarial-code-perturbations}}
}
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Contact

- **GitHub**: [@amanmukati09](https://github.com/amanmukati09)
- **Project Link**: [https://github.com/amanmukati09/adversarial-code-perturbations](https://github.com/amanmukati09/adversarial-code-perturbations)

---

## Acknowledgments

- CodeBERT model from Microsoft Research
- XGBoost library
- The open-source AI/ML community
