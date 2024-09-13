from mlProject.config.configuration import *

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def dowmload_file(self):
            