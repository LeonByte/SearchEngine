"""
SearchEngine: Multimodal search engine using CLIP embeddings
"""

__version__ = "0.1.0"
__author__ = "LeonByte"
__description__ = "Multimodal search engine for bidirectional image-text retrieval"

from . import embeddings, search, interface

__all__ = ["embeddings", "search", "interface"]