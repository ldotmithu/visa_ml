from src.mlProject.entity.config_entity import *
from mlProject import logging
from mlProject.utils.common import *
from mlProject.constants import *

class ConfiurationManager:
    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        
        create_directories([self.config.aritifact_root])
        
    def get_data_ingestion(self):
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            URL=config.URL,
            local_data_path=config.local_data_path,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_transfomation(self):
        config=self.config.data_transfomation
        
        create_directories([config.root_dir])
        
        data_transfomation_config=DataTransfomationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        
        return data_transfomation_config
    
    def get_model_train_config(self):
        config=self.config.model_training
        
        create_directories([config.root_dir])
        
        model_training_config=ModelTrainConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            train_data_path=config.train_data_path,
            model_name=config.model_name,
            preprocess_path=config.preprocess_path
        )
        
        return model_training_config
    
    def get_model_evaluation(self):
        config=self.config.model_evaluation
        
        create_directories([config.root_dir])
        
        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metric_file_path=config.metric_file_path,
            preprocess_path=config.preprocess_path
        )
        
        return model_evaluation_config
            
        
