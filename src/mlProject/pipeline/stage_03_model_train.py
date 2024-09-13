from mlProject.components.model_train import *
from mlProject import logging
from mlProject.config.configuration import *

class ModeltrainPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfiurationManager()
        model_training_config=config.get_model_train_config()
        model_training=ModelTrain(config=model_training_config)
        model_training.preprocess_method()
        model_training.train()