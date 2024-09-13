from mlProject.config.configuration import *
from mlProject import logging
from sklearn.preprocessing import OneHotEncoder, StandardScaler,OrdinalEncoder, PowerTransformer
from sklearn.compose import ColumnTransformer 
from sklearn.pipeline import Pipeline
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np 
import joblib
from mlProject.utils.common import *

class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
    def preprocess_method(self):
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
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
        traget_col='case_status'
        drop_col=['case_id','yr_of_estab']
        
        X_train=train_data.drop(columns=['case_status','case_id','yr_of_estab'],axis=1)
        X_test=test_data.drop(columns=[traget_col,drop_col],axis=1)
        y_train=train_data[traget_col]
        y_test=test_data[traget_col]
        
        preprocess_obj=self.preprocess_method()
        
        X_train=preprocess_obj.fit_transform(X_train)
        X_test=preprocess_obj.transform(X_test)
        
        rfc=RandomForestClassifier(n_estimators=100,max_depth=20,min_samples_split=5,min_samples_leaf=2,max_features='auto')
        
        joblib.load(rfc,os.path.join(self.config.root_dir,self.config.model_name))
        
        save_object(file_path=self.config.preprocess_path,obj=preprocess_obj)
        
        
        