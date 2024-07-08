#!/usr/bin/python3
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

fs = FileStorage()
fs1 = FileStorage()
print(type(fs.save))
file_path = "file.json"
try:
    file_path = FileStorage._FileStorage__file_path
except:
    pass

try:    
    os.remove(file_path)
except:
    pass

fs.new(BaseModel())
fs.save()
fs1.reload()
print(fs._FileStorage__objects == fs1._FileStorage__objects)
print(os.path.exists(file_path))
