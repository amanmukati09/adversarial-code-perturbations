"""
Central Configuration
All experiment parameters in one place for reproducibility.
"""

from pathlib import Path

# Paths
ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
CLEAN_DIR = DATA_DIR / "seed_samples" / "clean"
PERTURBED_DIR = DATA_DIR / "seed_samples" / "perturbed"
RESULTS_DIR = ROOT / "results"
FIGURES_DIR = ROOT / "paper" / "figures"

# Dataset
RANDOM_SEED = 42
TARGET_CLEAN_SAMPLES = 100
TARGET_PERTURBED_PER_CLEAN = 5  # 5 strategies per clean sample
TARGET_TOTAL = TARGET_CLEAN_SAMPLES + (TARGET_CLEAN_SAMPLES * TARGET_PERTURBED_PER_CLEAN)

# Model
EMBEDDING_MODEL = "microsoft/codebert-base"
MAX_SEQ_LENGTH = 512

# Training
CV_FOLDS = 5
TEST_SPLIT = 0.2  # hold out 20% for final evaluation
N_ESTIMATORS = 100
MAX_DEPTH = 4

# Perturbation strategies
STRATEGIES = [
    "boundary_invert",
    "variable_shadow",
    "import_alias",
    "dead_code",
    "comment_plant",
]

# Feature list (must match feature_extractor.py)
FEATURE_NAMES = [
    "code_length", "num_lines", "num_imports", "num_functions",
    "num_comments", "num_docstrings", "has_dead_code",
    "has_aliased_import", "variable_shadow_count", "ast_depth",
    "num_ast_nodes", "num_if_stmts", "num_loops", "num_try_blocks",
    "num_assignments", "num_calls", "parse_error",
]


def ensure_dirs():
    """Create all necessary directories."""
    for d in [DATA_DIR, CLEAN_DIR, PERTURBED_DIR, RESULTS_DIR, FIGURES_DIR]:
        d.mkdir(parents=True, exist_ok=True)
