---
license: other
task_categories:
  - text-classification
tags:
  - anomaly-detection
  - log-analysis
  - hdfs
pretty_name: HDFS v1 Block-Level Logs
size_categories:
  - 100K<n<1M
dataset_info:
  features:
  - name: block_id
    dtype: large_string
  - name: text
    dtype: large_string
  - name: label
    dtype: int8
  splits:
  - name: train
    num_bytes: 1106771219
    num_examples: 460048
  - name: dev
    num_bytes: 138246934
    num_examples: 57506
  - name: test
    num_bytes: 138610465
    num_examples: 57507
  download_size: 211196536
  dataset_size: 1383628618
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: dev
    path: data/dev-*
  - split: test
    path: data/test-*
---

# HDFS v1 Block-Level Dataset

## Dataset Summary

This dataset is a **block-level transformation** of the [HDFS_v1](https://huggingface.co/datasets/logfit-project/HDFS_v1) log dataset. While the original dataset contains individual log lines (~11M rows), this version aggregates all log entries belonging to the same block into a single text sequence, making it suitable for LLM-based anomaly classification.

Each row represents a unique HDFS block with its complete log history concatenated in chronological order.

## Supported Tasks

- **anomaly-detection**: Binary text classification to predict whether a block experienced an anomaly based on its log sequence.

## Dataset Structure

### Data Splits

| Split | Examples | Normal | Anomaly |
|-------|----------|--------|---------|
| train | 460,048  | 446,578 | 13,470 |
| dev   | 57,506   | 55,822  | 1,684  |
| test  | 57,507   | 55,823  | 1,684  |

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `block_id` | string | Unique HDFS block identifier (e.g., `blk_-1608999687919862906`) |
| `text` | string | Concatenated log entries for the block, newline-separated |
| `label` | int | Binary anomaly label (1 = anomalous, 0 = normal) |

### Text Format

Each log line within `text` follows the format:
```
<LEVEL> <COMPONENT>: <CONTENT>
```

Example:
```
INFO dfs.DataNode$DataXceiver: Receiving block blk_-1608999687919862906 src: /10.251.73.220:42557 dest: /10.251.73.220:50010
INFO dfs.DataNode$DataXceiver: Receiving block blk_-1608999687919862906 src: /10.251.73.220:55213 dest: /10.251.73.220:50010
INFO dfs.FSNamesystem: BLOCK* NameSystem.allocateBlock: /mnt/hadoop/mapred/system/job_200811092030_0001/job.jar. blk_-1608999687919862906
INFO dfs.DataNode$PacketResponder: PacketResponder 1 for block blk_-1608999687919862906 terminating
INFO dfs.DataNode$PacketResponder: Received block blk_-1608999687919862906 of size 67108864 from /10.251.73.220
```

## Source Data

- **Original Dataset**: [logfit-project/HDFS_v1](https://huggingface.co/datasets/logfit-project/HDFS_v1)
- **Original Source**: [LogPAI/loghub](https://github.com/logpai/loghub/tree/master/HDFS#hdfs_v1)

## Dataset Creation

1. Loaded the original line-level HDFS_v1 dataset
2. Formatted each log line as `<LEVEL> <COMPONENT>: <CONTENT>`
3. Grouped by `block_id` and concatenated log entries (ordered by line number)
4. Aggregated anomaly labels (max per block)
5. Created stratified 80/10/10 train/dev/test splits preserving class distribution

## Citation

```bibtex
@inproceedings{xu2009detecting,
  title={Detecting Large-Scale System Problems by Mining Console Logs},
  author={Xu, Wei and Huang, Ling and Fox, Armando and Patterson, David and Jordan, Michael},
  booktitle={SOSP 2009}
}

@inproceedings{zhu2023loghub,
  title={Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics},
  author={Zhu, Jieming and He, Shilin and He, Pinjia and Liu, Jinyang and Lyu, Michael R.},
  booktitle={ISSRE 2023}
}
```

## License

See original dataset license.