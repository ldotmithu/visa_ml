from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    URL: str
    local_data_path:Path
    unzip_dir:Path
    
@dataclass
class DataTransfomationConfig:
    root_dir:Path
    data_path:Path    
   
@dataclass
class ModelTrainConfig:
    root_dir:Path
    test_data_path:Path
    train_data_path:Path
    model_name:str
    preprocess_path:Path    