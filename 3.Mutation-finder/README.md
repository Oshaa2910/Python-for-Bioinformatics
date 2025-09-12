# Mutation Finder

A Python tool to compare a **normal gene sequence** vs. a **mutated gene sequence**. The script reads **FASTA files**, aligns sequences, highlights mutations visually, and classifies mutation types.

***Features***
- Reads sequences directly from **FASTA files**.
- **Aligns sequences** and highlights differences.
- Detects and classifies mutation types:
  - **Substitution** (e.g., A → G)
  - **Insertion** (extra base in mutated sequence)
  - **Deletion** (missing base in mutated sequence)
- Prints aligned sequences with mismatches marked by `*`.
