"""
Dataset Loader
Reads all clean and perturbed code samples, returns labeled pairs.
"""

from pathlib import Path

DATA_ROOT = Path(__file__).parent.parent / "data" / "seed_samples"


def load_all_samples():
    """
    Load all clean samples (label=0) and all perturbed samples (label=1).
    Returns list of dicts: {id, code, label}
    """
    samples = []
    clean_dir = DATA_ROOT / "clean"
    perturbed_dir = DATA_ROOT / "perturbed"

    # Load clean
    for clean_file in sorted(clean_dir.glob("*.py")):
        code = clean_file.read_text(encoding="utf-8")
        samples.append({
            "id": clean_file.stem,
            "code": code,
            "label": 0,
        })

    # Load perturbed
    for pert_file in sorted(perturbed_dir.glob("*.py")):
        code = pert_file.read_text(encoding="utf-8")
        samples.append({
            "id": pert_file.stem,
            "code": code,
            "label": 1,
        })

    return samples


if __name__ == "__main__":
    data = load_all_samples()
    clean_count = sum(1 for s in data if s["label"] == 0)
    perturbed_count = sum(1 for s in data if s["label"] == 1)
    print(f"Loaded {len(data)} total samples:")
    print(f"  Clean: {clean_count}")
    print(f"  Perturbed: {perturbed_count}")
    print("\nFirst 5:")
    for s in data[:5]:
        print(f"  {s['id']} -> label={s['label']}")
    print("...")
    print("Last 5:")
    for s in data[-5:]:
        print(f"  {s['id']} -> label={s['label']}")
