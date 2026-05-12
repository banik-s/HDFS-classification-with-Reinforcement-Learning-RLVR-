# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository demonstrates fine-tuning OpenAI's o4-mini model for HDFS log anomaly detection using Reinforcement Learning from Verifiable Rewards (RLVR). The project uses the HDFS_v1 dataset to train a binary classifier that identifies anomalous log blocks.

## Development Commands

```bash
# Install dependencies
uv sync

# Run Jupyter notebooks
uv run jupyter lab
```

## Environment Setup

Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_key_here
```

## Architecture

The project follows a three-notebook pipeline:

1. **1-data_prep.ipynb** - Transforms line-level HDFS logs into block-level format
   - Loads from `logfit-project/HDFS_v1` (11M log lines)
   - Aggregates logs by `block_id` into concatenated text
   - Creates stratified 80/10/10 train/dev/test splits
   - Pushes to HuggingFace Hub as `shawhin/HDFS_v1_blocks`

2. **2-model_training.ipynb** - Reinforcement fine-tuning via OpenAI API
   - Uses RLVR with a grader that scores model outputs
   - Target model: `o4-mini-2025-04-16`

3. **3-model_evaluation.ipynb** - Model evaluation on test set
   - Uses `functions.py` utilities for inference and metrics

## Utility Functions (functions.py)

- `run_inference(model_name, examples, response_format)` - Runs batch inference via OpenAI API with structured JSON responses
- `calculate_metrics(predictions, labels)` - Computes accuracy, precision, recall, and F1 score

## Dataset Schema

Each record in the block-level dataset contains:
- `block_id`: Unique HDFS block identifier
- `text`: Newline-separated log entries formatted as `<LEVEL> <COMPONENT>: <CONTENT>`
- `label`: Binary anomaly label (1 = anomalous, 0 = normal)

Note: The dataset is highly imbalanced (~97% normal, ~3% anomalous).

## Key Resources

- Dataset: https://huggingface.co/datasets/shawhin/HDFS_v1_blocks
- Original source: https://huggingface.co/datasets/logfit-project/HDFS_v1
