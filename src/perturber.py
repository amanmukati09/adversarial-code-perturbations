"""
Automated Perturber
Applies adversarial perturbations to Python code.
Strategies: boundary inversion, variable shadowing, import aliasing,
dead code insertion, commented-out malicious code, and more.
"""

import ast
import random
import re
from pathlib import Path

CLEAN_DIR = Path(__file__).parent.parent / "data" / "seed_samples" / "clean"
PERTURBED_DIR = Path(__file__).parent.parent / "data" / "seed_samples" / "perturbed"

STRATEGIES = [
    "boundary_invert",
    "variable_shadow",
    "import_alias",
    "dead_code",
    "comment_plant",
]


def perturb_boundary_invert(code: str) -> str:
    """Flip a comparison operator or boundary condition."""
    swaps = [
        ("<", "<="), (">=", ">"), ("==", "!="),
        ("len-1", "len"), ("len - 1", "len"),
        ('return "0"', 'return "1"'),
    ]
    for old, new in swaps:
        if old in code:
            return code.replace(old, new, 1)
    # Fallback: change a 0 to 1 in a return
    return re.sub(r"\breturn\s+0\b", "return 1", code, count=1)


def perturb_variable_shadow(code: str) -> str:
    """Add a variable reassignment that shadows a parameter."""
    # Find a function parameter name and shadow it
    match = re.search(r"def \w+\((\w+)", code)
    if not match:
        return code
    param = match.group(1)
    # Insert shadowing assignment before return
    shadow_line = f"    {param} = {param}  # shadowed"
    # Insert before the last return statement
    lines = code.split("\n")
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip().startswith("return "):
            lines.insert(i, shadow_line)
            break
    else:
        lines.append(shadow_line)
    return "\n".join(lines)


def perturb_import_alias(code: str) -> str:
    """Add a misleading import alias."""
    aliases = [
        ("from hashlib import md5 as sha256", "md5 as sha256"),
        ("from math import sqrt as isqrt", "sqrt as isqrt"),
        ("from os import urandom as random", "urandom as random"),
    ]
    alias_line, _ = random.choice(aliases)
    # Insert after last import or at top
    lines = code.split("\n")
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.strip().startswith(("import ", "from ")):
            insert_idx = i + 1
    lines.insert(insert_idx, alias_line)
    return "\n".join(lines)


def perturb_dead_code(code: str) -> str:
    """Insert a dead code block."""
    dead_block = "    if False:  # dead code, reviewer might uncomment\n        pass"
    # Insert inside function body
    lines = code.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("def "):
            # Insert after first non-docstring line in function
            for j in range(i + 1, len(lines)):
                if lines[j].strip() and not lines[j].strip().startswith(('"""', "'''", "#")):
                    lines.insert(j, dead_block)
                    return "\n".join(lines)
    return code


def perturb_comment_plant(code: str) -> str:
    """Insert a commented-out dangerous line."""
    comment_lines = [
        "    # if len(data) > 1000: return []  # early exit, commented out",
        "    # result = result[::-1]  # reverse result, commented out",
        "    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger",
    ]
    chosen = random.choice(comment_lines)
    lines = code.split("\n")
    # Insert near middle of function
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip().startswith("return "):
            lines.insert(i, chosen)
            break
    else:
        lines.insert(len(lines) // 2, chosen)
    return "\n".join(lines)


def apply_perturbation(code: str, strategy: str) -> str:
    """Apply a single perturbation strategy to the code."""
    if strategy == "boundary_invert":
        return perturb_boundary_invert(code)
    elif strategy == "variable_shadow":
        return perturb_variable_shadow(code)
    elif strategy == "import_alias":
        return perturb_import_alias(code)
    elif strategy == "dead_code":
        return perturb_dead_code(code)
    elif strategy == "comment_plant":
        return perturb_comment_plant(code)
    return code


def perturb_all_samples(overwrite: bool = True) -> int:
    """
    For each clean sample, generate perturbed versions using all strategies.
    Saves as sample_XX_{strategy}.py in perturbed directory.
    """
    PERTURBED_DIR.mkdir(parents=True, exist_ok=True)
    count = 0

    for clean_file in sorted(CLEAN_DIR.glob("*.py")):
        sample_id = clean_file.stem
        original_code = clean_file.read_text(encoding="utf-8")

        for strategy in STRATEGIES:
            out_file = PERTURBED_DIR / f"{sample_id}_{strategy}.py"
            if out_file.exists() and not overwrite:
                continue

            perturbed_code = apply_perturbation(original_code, strategy)
            if perturbed_code != original_code:
                out_file.write_text(perturbed_code, encoding="utf-8")
                count += 1

    return count


if __name__ == "__main__":
    print("=== Generating perturbed samples ===\n")
    n = perturb_all_samples(overwrite=True)
    print(f"\nDone. Generated {n} perturbed samples.")
