"""
Code Generator Module
Uses Gemini API to generate Python functions from prompts.
Saves generated code to data/seed_samples/clean/.
"""

import os
import time
from pathlib import Path
import google.generativeai as genai

# Configure Gemini
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable not set.")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

SEED_PROMPTS = [
    "Write a Python function to validate an email address. Only output the code, no explanation.",
    "Write a Python function to merge two sorted lists. Only output the code, no explanation.",
    "Write a Python function to parse a CSV file and return column averages. Only output the code, no explanation.",
    "Write a Python function to check if a string is a palindrome. Only output the code, no explanation.",
    "Write a Python function to compute the factorial of a number. Only output the code, no explanation.",
    "Write a Python function to flatten a nested list recursively. Only output the code, no explanation.",
    "Write a Python function to count word frequency in a text. Only output the code, no explanation.",
    "Write a Python function to find the longest common prefix of two strings. Only output the code, no explanation.",
    "Write a Python function to convert a decimal integer to binary string. Only output the code, no explanation.",
    "Write a Python function to check if a number is prime. Only output the code, no explanation.",
    "Write a Python function to compute the Fibonacci sequence up to n terms. Only output the code, no explanation.",
    "Write a Python function to reverse a linked list. Only output the code, no explanation.",
    "Write a Python function to find the maximum subarray sum (Kadane's algorithm). Only output the code, no explanation.",
    "Write a Python function to implement binary search on a sorted list. Only output the code, no explanation.",
    "Write a Python function to check if two strings are anagrams. Only output the code, no explanation.",
    "Write a Python function to remove duplicates from a list while preserving order. Only output the code, no explanation.",
    "Write a Python function to compute the greatest common divisor (GCD) using Euclidean algorithm. Only output the code, no explanation.",
    "Write a Python function to rotate a list by k positions. Only output the code, no explanation.",
    "Write a Python function to find the intersection of two lists. Only output the code, no explanation.",
    "Write a Python function to implement a simple caching decorator (memoization). Only output the code, no explanation.",
]

CLEAN_DIR = Path(__file__).parent.parent / "data" / "seed_samples" / "clean"


def generate_code(prompt: str, retries: int = 2) -> str:
    """Call Gemini to generate code, with retries on failure."""
    for attempt in range(retries + 1):
        try:
            response = model.generate_content(prompt)
            code = response.text.strip()
            # Clean up markdown code blocks if present
            if code.startswith("```"):
                code = "\n".join(code.split("\n")[1:-1])
            return code
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}")
            if attempt < retries:
                time.sleep(2)
    return ""


def generate_all(overwrite: bool = False) -> int:
    """Generate code for all prompts, save as sample_XX.py."""
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    count = 0

    for i, prompt in enumerate(SEED_PROMPTS, 1):
        filename = f"sample_{i:02d}.py"
        filepath = CLEAN_DIR / filename

        if filepath.exists() and not overwrite:
            print(f"[{i:02d}] Skipping (already exists): {filename}")
            continue

        print(f"[{i:02d}] Generating: {prompt[:60]}...")
        code = generate_code(prompt)

        if code:
            filepath.write_text(code, encoding="utf-8")
            print(f"      Saved to {filename} ({len(code)} chars)")
            count += 1
        else:
            print(f"      FAILED to generate")

        time.sleep(0.5)  # rate limit safety

    return count


if __name__ == "__main__":
    print("=== Generating clean code samples via Gemini ===\n")
    n = generate_all(overwrite=False)  # won't overwrite our 10 hand-crafted samples
    print(f"\nDone. Generated {n} new samples.")
