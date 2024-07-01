#!/usr/bin/python3
from engine import file_storage

__all__ = [
        "base_model" # 'base_model.py' file
]
storage = file_storage.FileStorage()
storage.reload()
