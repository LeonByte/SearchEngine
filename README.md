# SearchEngine

**Multimodal search engine using CLIP embeddings for bidirectional image-text retrieval.**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.6+-red.svg)](https://pytorch.org/)
[![CUDA](https://img.shields.io/badge/CUDA-12.4+-green.svg)](https://developer.nvidia.com/cuda-downloads)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Local-First](https://img.shields.io/badge/Local--First-Privacy--Focused-green.svg)](https://www.inkandswitch.com/local-first/)

Built for local deployment on **NVIDIA RTX 4060 (8GB VRAM)** with Poetry dependency management and optimized for educational purposes.

## Features

### Core Functionality
- **Text-to-Image Search**: Find images using natural language descriptions
- **Image-to-Text Search**: Find text descriptions using image queries  
- **Local-First**: All processing runs locally, no API calls or cloud dependencies
- **FOSS Stack**: 100% Free and Open Source Software
- **GPU Optimized**: Efficient inference on consumer hardware (RTX 4060)
- **Web Interface**: Gradio-based interface for easy interaction

### Technical Highlights
- **CLIP ViT-B/16**: Optimal accuracy-to-performance ratio for 8GB VRAM
- **FP16 Mixed Precision**: 40-50% memory reduction with faster inference
- **Batch Processing**: Optimized throughput with dynamic batch sizing
- **Similarity Search**: Fast cosine similarity with scikit-learn (FAISS optional)
- **Memory Management**: Proper CUDA cache handling for stable operation

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Model** | CLIP ViT-B/16 | Multimodal embeddings for text and images |
| **Framework** | sentence-transformers + PyTorch | CLIP model loading and inference |
| **Similarity Search** | scikit-learn + FAISS (optional) | Fast similarity computation |
| **Interface** | Gradio | Interactive web interface |
| **Dataset** | Flickr8k | 8,000 images with captions |
| **Environment** | Python 3.12+ & Poetry | Dependency management |

## Quick Start

### Prerequisites

- **Python 3.12+** installed
- **NVIDIA GPU with 8GB+ VRAM** (tested on RTX 4060)
- **CUDA 12.4+ drivers** 
- **Poetry 2.1.4+** for dependency management

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SearchEngine
   ```

2. **Install dependencies with Poetry**
   ```bash
   poetry install
   ```

3. **Activate the environment**
   ```bash
   # Show activation command
   poetry env activate
   
   # Or use the path directly
   source $(poetry env info --path)/bin/activate

   # Alternately, use the full path shown by 'poetry env activate'
   source /path/to/your/virtualenv/bin/activate  
   ```

4. **Verify GPU setup**
   ```bash
   poetry run python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"None\"}')"
   ```

### Download Dataset

The Flickr8k dataset will be automatically downloaded during the first notebook execution. Alternatively, download manually:

```bash
# Using Kaggle API (requires kaggle account and API key)
kaggle datasets download -d adityajn105/flickr8k
```

## Project Structure

```
SearchEngine/
├── notebooks/                   # Jupyter notebooks for each part
│   ├── 01_data_preparation.ipynb      # Part 1: Data loading & embedding
│   ├── 02_search_functionality.ipynb  # Part 2: Search implementation  
│   └── 03_multimodal_interface.ipynb  # Part 3: Web interface
├── src/                        # Reusable Python modules
│   ├── __init__.py
│   ├── embeddings.py           # Embedding generation utilities
│   ├── search.py              # Search functionality
│   └── interface.py           # Gradio interface components
├── data/                       # Dataset and processed files
│   ├── raw/                   # Original Flickr8k data
│   ├── processed/             # Generated embeddings & indices
│   └── sample/               # Sample images for testing
├── outputs/                    # Generated outputs
│   └── pdfs/                  # Exported notebook PDFs
├── pyproject.toml             # Poetry dependencies
├── README.md                  # This file
└── .gitignore                # Git ignore patterns
```

## Performance Expectations

**RTX 4060 8GB VRAM:**
- **Embedding Generation**: ~2-3 hours for full Flickr8k dataset
- **Search Speed**: <2ms per query with FAISS indexing
- **Memory Usage**: ~2GB peak during batch processing
- **Throughput**: 1,200-1,500 images/second with optimization

## Development Workflow

### Running Notebooks

Execute notebooks in sequence:

```bash
# Start Jupyter Lab
jupyter lab

# Or individual notebooks
jupyter notebook notebooks/01_data_preparation.ipynb
```

### Code Development

Reusable code lives in `src/` modules:

```python
from src.embeddings import CLIPEmbedder
from src.search import MultimodalSearch
from src.interface import create_gradio_app
```

### Committing Changes

Follow atomic commit practices:
```bash
git add <specific-files>
git commit -m "feat: add embedding generation utilities"
```

## Optimization Settings

The project is optimized for RTX 4060 with these key settings:

- **Mixed Precision (FP16)**: 40-50% memory reduction
- **Batch Size**: 64 images (optimal for 8GB VRAM)
- **Model**: ViT-B/16 (best accuracy/performance ratio)
- **FAISS**: GPU-accelerated similarity search

## Deliverables

For university submission:
- ✅ 3 executable Jupyter notebooks (error-free)
- ✅ PDF exports of executed notebooks
- ✅ Working Gradio web interface
- ✅ All outputs visible without re-running

## Memory Management

Key practices for stable operation:
- Enable `torch.no_grad()` during inference
- Clear CUDA cache between batches: `torch.cuda.empty_cache()`
- Monitor VRAM usage: keep below 7GB for stable operation
- Use context managers for model loading

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make atomic commits with descriptive messages
4. Test on RTX 4060 hardware
5. Submit a pull request

---

**Note**: This project is designed for educational purposes and local deployment. All models and data processing run locally without external API dependencies.

---

<div align="center">
  <sub>Built with ❤️ for AI education • <a href="#quick-start">Get Started</a> • <a href="https://github.com/LeonByte/SearchEngine/issues">Report Bug</a> • <a href="https://github.com/LeonByte/SearchEngine/issues">Request Feature</a></sub>
</div>