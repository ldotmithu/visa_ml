from mlProject.config.configuration import *
from sklearn.metrics import accuracy_score
import pandas as pd 

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
        
        X_test=
            