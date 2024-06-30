# Phylogenetic Tree Construction for SSU (16s rRNA) Sequences

This document provides a detailed guide for creating a phylogenetic tree using SSU (16s rRNA) sequences. The workflow includes sequence alignment with MAFFT, phylogenetic analysis with RAxML, sequence preprocessing with Python, and automation using Snakemake.

## Introduction

The aim of this project is to construct a phylogenetic tree for SSU (16s rRNA) sequences to analyze evolutionary relationships. We use MAFFT for multiple sequence alignment, RAxML for building the phylogenetic tree, Python for sequence preprocessing tasks, and Snakemake to automate the workflow.

## Workflow

1. **Data Preparation**: Collect and preprocess 16s rRNA sequences.
2. **Sequence Alignment**: Align sequences using MAFFT.
3. **Phylogenetic Analysis**: Build a phylogenetic tree using RAxML.
4. **Merging and Filtering**: Merge and filter sequences using Python.
5. **Automation**: Use Snakemake to automate the pipeline.

## Tools Used

- **Python 3.x**: For sequence preprocessing
- **MAFFT**: For sequence alignment
- **RAxML**: For phylogenetic analysis
- **Biopython**: For handling sequences in Python 
- **Snakemake**: For workflow automation 

