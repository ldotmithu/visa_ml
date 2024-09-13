from mlProject.components.data_transfomation import *
from mlProject.config.configuration import *

class DataTransfomationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfiurationManager()
        data_transfomation_config=config.get_data_transfomation()
        data_transfomation=DataTransfomation(config=data_transfomation_config)
        data_transfomation.split_data()