"""
AST Feature Extractor
Extracts structural features from Python code for perturbation detection.
No execution — purely static analysis.
"""

import ast
import re


def extract_features(code: str) -> dict:
    """
    Parse Python code and extract structural features.
    Returns a dictionary of numerical features.
    """
    features = {}

    # Basic text features (no parsing needed)
    features["code_length"] = len(code)
    features["num_lines"] = len(code.splitlines())
    features["num_imports"] = len(re.findall(r"^\s*(import|from)\s", code, re.MULTILINE))
    features["num_functions"] = len(re.findall(r"^\s*def\s", code, re.MULTILINE))
    features["num_comments"] = len(re.findall(r"#", code))
    features["num_docstrings"] = len(re.findall(r'"""', code)) // 2

    # Check for suspicious patterns
    features["has_dead_code"] = 1 if re.search(r"if\s+False\s*:", code) else 0
    features["has_aliased_import"] = 1 if re.search(r"import\s+\w+\s+as\s+\w+", code) else 0
    features["variable_shadow_count"] = len(
        re.findall(r"(\w+)\s*=\s*.*\1", code)
    )

    # AST-based features
    try:
        tree = ast.parse(code)

        features["ast_depth"] = _get_ast_depth(tree)
        features["num_ast_nodes"] = len(list(ast.walk(tree)))
        features["num_if_stmts"] = len([n for n in ast.walk(tree) if isinstance(n, ast.If)])
        features["num_loops"] = len(
            [n for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While))]
        )
        features["num_try_blocks"] = len([n for n in ast.walk(tree) if isinstance(n, ast.Try)])
        features["num_assignments"] = len([n for n in ast.walk(tree) if isinstance(n, ast.Assign)])
        features["num_calls"] = len([n for n in ast.walk(tree) if isinstance(n, ast.Call)])
        features["parse_error"] = 0

    except SyntaxError:
        features["ast_depth"] = 0
        features["num_ast_nodes"] = 0
        features["num_if_stmts"] = 0
        features["num_loops"] = 0
        features["num_try_blocks"] = 0
        features["num_assignments"] = 0
        features["num_calls"] = 0
        features["parse_error"] = 1

    return features


def _get_ast_depth(node, depth=0):
    """Recursively compute max depth of AST."""
    if not hasattr(node, "body"):
        return depth
    max_depth = depth
    for child in ast.iter_child_nodes(node):
        child_depth = _get_ast_depth(child, depth + 1)
        max_depth = max(max_depth, child_depth)
    return max_depth


if __name__ == "__main__":
    # Quick test on our seed samples
    from pathlib import Path

    clean_dir = Path(__file__).parent.parent / "data" / "seed_samples" / "clean"
    perturbed_dir = Path(__file__).parent.parent / "data" / "seed_samples" / "perturbed"

    print("=== CLEAN ===")
    for f in sorted(clean_dir.glob("*.py")):
        code = f.read_text()
        feats = extract_features(code)
        print(f"\n{f.name}:")
        for k, v in feats.items():
            print(f"  {k}: {v}")

    print("\n=== PERTURBED ===")
    for f in sorted(perturbed_dir.glob("*.py")):
        code = f.read_text()
        feats = extract_features(code)
        print(f"\n{f.name}:")
        for k, v in feats.items():
            print(f"  {k}: {v}")
