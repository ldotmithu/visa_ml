from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_transfomation import DataTransfomationPipeline
from mlProject.pipeline.stage_03_model_train import ModeltrainPipeline
from mlProject.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
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

Stage_name='Model Train'
try:
    model_training=ModeltrainPipeline()
    model_training.main()
    logging.info('Model Train Completed')
except Exception as e:
    logging.exception(e)
    raise e  

Stage_name='Model evaluation'
try:
    model_evaluation=ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info('Model evaluation Completed')
except Exception as e:
    logging.exception(e)
    raise e  

