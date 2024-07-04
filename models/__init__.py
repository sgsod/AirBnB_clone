
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
__all__ = [
        "base_model",# 'base_model.py' file
]
