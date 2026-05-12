# RLVR for HDFS Classification

Example code for fine-tuning o4-mini to do anomaly detection of HDFS logs using Reinforcement Learning from Verifiable Rewards (RLVR).

**Resources:**
- [Video Explainer](https://youtu.be/k-94oCJ_WJo)
- [GitHub Repo](https://github.com/ShawhinT/rlvr-hdfs-classification)
- [Dataset](https://huggingface.co/datasets/shawhin/HDFS_v1_blocks)

## Setup

1. Clone the repo and navigate to it:
   ```bash
   git clone https://github.com/ShawhinT/rlvr-hdfs-classification.git
   cd rlvr-hdfs-classification
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```bash
   cp .env.example .env
   ```

4. Run Jupyter notebooks:
   ```bash
   uv run jupyter lab
   ```

## Workflow

1. **Data Prep** (`1-data_prep.ipynb`) - Transforms HDFS logs into block-level format with train/dev/test splits
2. **Training** (`2-model_training.ipynb`) - Fine-tunes o4-mini using RLVR via OpenAI API
3. **Evaluation** (`3-model_evaluation.ipynb`) - Evaluates model performance on test set
