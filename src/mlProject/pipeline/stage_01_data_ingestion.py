from mlProject.components.data_ingestion import *
from mlProject.config.configuration import *

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfiurationManager()
        data_ingestion_config=config.get_data_ingestion()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.dowmload_file()
        data_ingestion.extract_file()