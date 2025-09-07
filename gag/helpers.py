import os 
from datetime import datetime
from typing import dataclass_transform
from django.utils.deconstruct import deconstructible

@deconstructible  
class UploadTo:
    def __init__(self, folder):
        self.folder = folder
        
    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[1]
        now = datetime.now()
        
        return "{}/{:%Y-%m}/{:%Y-%m-%d-%H-%M-%S}{}".format(
            self.folder,
            now,  # 1-{} va {:%Y-%m} uchun
            now,  # 2-{:%Y-%m-%d-%H-%M-%S} uchun
            ext   # 3-{} uchun
        )


