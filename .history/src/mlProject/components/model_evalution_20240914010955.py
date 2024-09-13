from mlProject.config.configuration import *

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig) -> None:
        self.config=config
        
    def eval_metrics(self):
            