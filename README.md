# Persian Synthetic Data Generation

This repository contains code and resources for generating high-quality synthetic data in Persian language using State-of-the-Art Language Models (LLMs).

## Overview

This project provides tools and utilities to generate synthetic Persian text data using advanced language models. It includes predefined topic trees, prompts, and datasets that can be used to generate domain-specific Persian content.

## Project Structure

```
.
├── datasets/                  # Generated synthetic datasets
├── prompts/                  # Prompt templates and configurations
│   └── topic_prompts.json
├── topic_trees/             # Topic hierarchies and structures
├── gen_synthetic.py         # Main synthetic data generation script
├── gen_synthetic_emotions.py # Emotion-specific data generation
└── Experience.ipynb         # Example notebook with usage demonstrations
```

## Prerequisites

- Python 3.x
- UV package manager
- Required API keys (see Environment Variables)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ParsBench/PersianSyntheticData.git
cd PersianSyntheticData
```

2. Install dependencies using UV:
```bash
uv venv
source .venv/bin/activate  # On Unix-like systems
# or
.venv\Scripts\activate     # On Windows
uv pip install -r requirements.txt
```

## Environment Variables

Copy the `.env.sample` file to create your own `.env`:

```bash
cp .env.sample .env
```

Configure the following variables in your `.env` file:
- Add your API keys and other configuration parameters

## Usage

### Basic Data Generation

Run the main generation script:

```bash
python gen_synthetic.py
```

### Emotion-Specific Data Generation

For generating emotion-related synthetic data:

```bash
python gen_synthetic_emotions.py
```

## Project Components

- **Topic Trees**: Hierarchical structures defining the relationships between different Persian topics
- **Prompts**: Carefully crafted prompt templates for generating contextually relevant data
- **Datasets**: Generated synthetic data in JSONL format
- **Notebooks**: Interactive examples and demonstrations in Jupyter notebooks

## License

This project is licensed under the Apache License 2.0 - see below for details:
```
Copyright 2024 ParsBench

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

For the full license text, please see the [LICENSE](LICENSE) file in the repository.

## Citation

If you use this project in your research, please cite:

```bibtex
@misc{parsbench2025,
  title={ParsBench: A Framework for Generating High-Quality Persian Language Datasets},
  author={ParsBench Team, Shariati Shahriar},
  year={2025},
  publisher={GitHub},
  howpublished={\url{https://github.com/ParsBench/PersianSyntheticData}},
  note={Open-source framework for Persian language dataset generation}
}
```

## Acknowledgments

- Special thanks to [AvalAI](https://avalai.ir/) for sponsoring this project through their AvalAward program
- This repository was made possible by AvalAI's generous support and commitment to advancing Persian language AI research

