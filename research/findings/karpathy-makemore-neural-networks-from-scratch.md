---
title: "Karpathy: makemore and Neural Networks from Scratch"
tags: [neural-networks, karpathy, backpropagation, micrograd, deep-learning, education]
related: [[agent-memory]], [[context-stack]], [[per-run-learning]], [[synthesis-over-retrieval]]
source: research/raw/karpathy-makemore-neural-networks-from-scratch.md
---

# Karpathy: makemore and Neural Networks from Scratch

Andrej Karpathy's "makemore" series builds neural networks from a blank Jupyter notebook. Starting with `micrograd` — a tiny automatic differentiation engine — he constructs and trains multi-layer perceptrons.

## Core Thesis

Neural networks are just mathematical expressions. Backpropagation is the chain rule from calculus applied recursively. Nothing more.

## The Atomic Unit: The Value Object

At the heart of `micrograd` is a `Value` object wrapping a scalar:
- `data`: the actual numerical value
- `grad`: the local derivative
- `_prev`: child nodes that created this value
- `_op`: the operation that produced it

This scalar-level approach is excessive for production but perfect for pedagogy. It breaks neural nets into atoms.

## Backpropagation is Just the Chain Rule

- **Forward pass:** build the expression graph, compute the output
- **Backward pass:** start at the output, move backward, apply local derivative at each node
- **Goal:** find how nudging each weight slightly in a positive direction changes the final loss

## Neural Networks are Mathematical Expressions

A neural network is a specific class of mathematical expression. Inputs and weights pass through layers of neurons (`sum(weights * inputs) + bias` followed by a non-linearity like `tanh`), producing a loss. `micrograd` doesn't know about "neural nets" — it just differentiates math.

## Efficiency vs. Understanding

Production libraries like PyTorch use tensors (n-dimensional arrays). The math doesn't change. Tensors are an efficiency hack for GPU parallelism. Understanding the scalar version is the key to understanding the tensor version.

## Implications for Agent Systems

- **Agents are expression graphs:** an agent's thought process is a forward pass through prompts and tools
- **Optimization is local:** improve agents by looking at the "local derivative" of performance — what small change yields a better outcome
- **Substrate matters:** just as `micrograd` is the substrate for neural nets, the knowledge graph is the substrate for agents. The "backward pass" (learning from mistakes) must be as robust as the forward pass
