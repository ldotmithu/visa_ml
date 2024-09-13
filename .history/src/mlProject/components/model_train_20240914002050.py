from mlProject.config.configuration import *
from mlProject import logging
from sklearn.preprocessing import OneHotEncoder, StandardScaler,OrdinalEncoder, PowerTransformer
from sklearn.compose import ColumnTransformer 
from sklearn.pipeline import Pipeline

class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
    def preprocess(self):
        try:
            or_columns = ['has_job_experience','requires_job_training','full_time_position','education_of_employee']
            oh_columns = ['continent','unit_of_wage','region_of_employment']
            transform_columns= ['no_of_employees','company_age']
            num_features=['no_of_employees','prevailing_wage','company_age']
            
            numeric_transformer = StandardScaler()
            oh_transformer = OneHotEncoder()
            ordinal_encoder = OrdinalEncoder()
            
            transform_pipe = Pipeline(steps=[
            ('transformer', PowerTransformer(method='yeo-johnson'))
            ])

            preprocessor = ColumnTransformer(
                [
                    ("OneHotEncoder", oh_transformer, oh_columns),
                    ("Ordinal_Encoder", ordinal_encoder, or_columns),
                    ("Transformer", transform_pipe, transform_columns),
                    ("StandardScaler", numeric_transformer, num_features)
                ]
            )
            return preprocessor
            
        except Exception as e:
            logging.exception(e)
            raise e
        
    def train(self):    