# Hypothesis

AI-generated code contains systematic vulnerabilities that are:
1. Not random — they follow patterns tied to how models reason about code
2. Exploitable via structured, minimal perturbations
3. Hard to detect with standard static analysis

We propose that a learned detector, trained on structural features
(AST patterns, data flow edges) and embeddings, can distinguish
adversarially-perturbed code from clean AI-generated code —
even when the perturbation is invisible to human reviewers.

## Research Questions
1. What perturbation strategies most reliably fool AI code reviewers?
2. Can AST features catch what embedding models miss, and vice versa?
3. Does the detector generalize across different code generation models?
4. Can the detector itself be evaded by adversarial perturbations?

## Success Metric
A classifier that achieves >80% accuracy on held-out perturbed/clean pairs,
and generalizes to at least one unseen code generation model.
