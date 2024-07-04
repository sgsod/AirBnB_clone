#!/usr/bin/python3
from base_model import BaseModel
from datetime import datetime

bm1 = BaseModel()
bm2 = BaseModel(**bm1.to_dict())
print(bm1.created_at == bm2.created_at)
print(bm1.created_at)
print(bm2.created_at)
