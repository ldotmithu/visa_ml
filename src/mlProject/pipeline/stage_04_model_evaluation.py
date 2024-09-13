from mlProject.components.model_evalution import *
from mlProject.config.configuration import *


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfiurationManager()
        model_evaluation_config=config.get_model_evaluation()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.save_result()