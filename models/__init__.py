#!/usr/bin/python3
from engine.file_storage import FileStorage

__all__ = [
        "base_model" # 'base_model.py' file
]
storage = FileStorage()
storage.reload()
