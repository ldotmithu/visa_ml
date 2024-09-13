from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_transfomation import DataTransfomationPipeline
from mlProject import logging

Stage_name='Data Ingestion'
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info('Data Ingestion Completed')
except Exception as e:
    logging.exception(e)
    raise e    


Stage_name='Data Transfomation'
try:
    data_transfomation=DataTransfomationPipeline()
    data_transfomation.main()
    logging.info('Data Transfomation Completed')
except Exception as e:
    logging.exception(e)
    raise e  