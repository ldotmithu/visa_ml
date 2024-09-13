from mlProject.config.configuration import *
from sklearn.metrics import accuracy_score
import pandas as pd 
import numpy as np 
from mlProject import logging
from mlProject.utils.common import save_json

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig) -> None:
        self.config=config
        
    def eval_metrics(self,actual,pred):
        acc_score=accuracy_score(actual,pred)
        
        return acc_score
    
    def save_result(self):
        test_data=pd.read_csv(self.config.test_data_path)
        
        model=joblib.load(self.config.model_path)
        preprocess_obj=self.config.preprocess_path
        
        target_col = 'case_status'
        X_test = test_data.drop(columns=['case_status', 'case_id', 'yr_of_estab'], axis=1)
        y_test = test_data[target_col]
        
        y_test= np.where(y_test=='Denied', 1,0)
        
        X_test=preprocess_obj.transform(X_test)
        
        prd=model.predict(X_test)
        
        acc_score=self.eval_metrics(y_test,prd)
        logging.info(acc_score)
        
        score={'acc_score':acc_score}
        save_json(Path(self.config.metric_file_path),data=score)
        
        
        
        
        
            