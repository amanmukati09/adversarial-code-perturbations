"""
Figure Generator
Creates publication-quality figures for the paper.
Outputs: paper/figures/detector_comparison.png and paper/figures/strategy_heatmap.png
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

FIGURES_DIR = Path(__file__).parent.parent / "paper" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
})


def plot_detector_comparison():
    """Figure 1: Bar chart comparing three detectors."""
    detectors = ['AST Features\n+ XGBoost', 'CodeBERT\n+ LogReg', 'Ensemble\n(AST + Embeddings)']
    accuracy = [0.91, 0.87, 0.87]
    precision = [0.96, 0.91, 0.92]
    recall = [0.93, 0.93, 0.92]

    x = np.arange(len(detectors))
    width = 0.25

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar(x - width, accuracy, width, label='Accuracy', color='#2E86AB', edgecolor='black', linewidth=0.5)
    bars2 = ax.bar(x, precision, width, label='Precision', color='#A23B72', edgecolor='black', linewidth=0.5)
    bars3 = ax.bar(x + width, recall, width, label='Recall', color='#F18F01', edgecolor='black', linewidth=0.5)

    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),
                       textcoords="offset points",
                       ha='center', va='bottom', fontsize=9)

    ax.set_xlabel('Detection Approach', fontweight='bold')
    ax.set_ylabel('Score', fontweight='bold')
    ax.set_title('Detection Performance Comparison (N=550)', fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(detectors)
    ax.set_ylim(0, 1.1)
    ax.legend(loc='lower right', frameon=True, fancybox=True, shadow=True)
    ax.grid(axis='y', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    output_path = FIGURES_DIR / "detector_comparison.png"
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")


def plot_strategy_heatmap():
    """Figure 2: Heatmap showing per-strategy detection performance."""
    strategies = ['Comment\nPlanting', 'Dead Code\nInsertion', 'Variable\nShadowing', 'Import\nAliasing', 'Boundary\nInversion']
    metrics = ['AST Features\n(Leave-One-Out)', 'CodeBERT\nEmbeddings']
    
    # Data: [AST LOSO recall, CodeBERT recall]
    data = np.array([
        [1.00, 0.95],   # Comment planting
        [1.00, 0.92],   # Dead code
        [1.00, 0.89],   # Variable shadowing
        [0.07, 0.55],   # Import aliasing
        [0.00, 0.48],   # Boundary inversion
    ])

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(data.T, cmap='RdYlGn', vmin=0, vmax=1, aspect='auto')

    # Add text annotations
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            text_color = 'black' if 0.3 < data[i, j] < 0.7 else 'white'
            ax.text(i, j, f'{data[i, j]:.2f}', ha='center', va='center', fontsize=12, fontweight='bold', color=text_color)

    # Set ticks
    ax.set_xticks(np.arange(len(strategies)))
    ax.set_xticklabels(strategies, fontsize=10)
    ax.set_yticks(np.arange(len(metrics)))
    ax.set_yticklabels(metrics, fontsize=10)

    # Labels
    ax.set_xlabel('Perturbation Strategy', fontweight='bold')
    ax.set_title('Per-Strategy Detection Recall\n(Red = Undetectable, Green = Detected)', fontweight='bold', pad=15)

    # Colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Recall Score', fontweight='bold')

    # Add tier labels
    ax.text(-0.5, -0.3, 'Tier 1: Trivially Detected', fontsize=9, fontweight='bold', color='green')
    ax.text(3.5, -0.3, 'Tier 3: Invisible', fontsize=9, fontweight='bold', color='red')

    plt.tight_layout()
    output_path = FIGURES_DIR / "strategy_heatmap.png"
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")


def plot_feature_importance():
    """Figure 3: Feature importance from XGBoost."""
    features = [
        'Number of Comments', 'Has Aliased Import', 'Number of Function Calls',
        'AST Node Count', 'AST Depth', 'Number of Assignments',
        'Number of If Statements', 'Code Length', 'Number of Imports',
        'Number of Loops', 'Number of Lines', 'Variable Shadow Count',
        'Number of Functions', 'Number of Docstrings', 'Has Dead Code',
        'Number of Try Blocks', 'Parse Error'
    ]
    importances = [0.545, 0.430, 0.005, 0.003, 0.003, 0.003, 0.003, 0.002, 0.002, 0.002, 0.002, 0.002, 0.000, 0.000, 0.000, 0.000, 0.000]

    # Sort by importance
    sorted_indices = np.argsort(importances)
    sorted_features = [features[i] for i in sorted_indices]
    sorted_importances = [importances[i] for i in sorted_indices]

    fig, ax = plt.subplots(figsize=(10, 8))
    bars = ax.barh(sorted_features, sorted_importances, color='#2E86AB', edgecolor='black', linewidth=0.5)
    
    # Highlight top features
    bars[-1].set_color('#F18F01')
    bars[-2].set_color('#F18F01')

    ax.set_xlabel('Feature Importance', fontweight='bold')
    ax.set_title('XGBoost Feature Importances\n(Top 2 features dominate detection)', fontweight='bold', pad=15)
    ax.grid(axis='x', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    output_path = FIGURES_DIR / "feature_importance.png"
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    print("Generating figures...")
    plot_detector_comparison()
    plot_strategy_heatmap()
    plot_feature_importance()
    print("\nAll figures generated successfully!")
