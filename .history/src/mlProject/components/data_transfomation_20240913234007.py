from mlProject.config.configuration import *
from mlProject import logging
import pandas as ps 
import os 
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self,config:DataTransfomationConfig):
        self.config=config
        
        