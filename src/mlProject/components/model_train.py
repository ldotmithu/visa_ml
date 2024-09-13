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
from sklearn.model_selection import RandomizedSearchCV

class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
    def preprocess_method(self):
        try:
            or_columns = ['has_job_experience','requires_job_training','full_time_position','education_of_employee']
            oh_columns = ['continent','unit_of_wage','region_of_employment']
            transform_columns= ['no_of_employees']
            num_features=['no_of_employees','prevailing_wage']
            
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
        try:
            # Load the datasets
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)

            target_col = 'case_status'

            # Separate features and target labels
            X_train = train_data.drop(columns=['case_status', 'case_id', 'yr_of_estab'], axis=1)
            X_test = test_data.drop(columns=['case_status', 'case_id', 'yr_of_estab'], axis=1)
            y_train = train_data[target_col]
            y_test = test_data[target_col]

            # Preprocess the data
            preprocess_obj = self.preprocess_method()

            # Fit and transform the training data
            X_train = preprocess_obj.fit_transform(X_train)
            X_test = preprocess_obj.transform(X_test)

            # Define the RandomForestClassifier
            rfc = RandomForestClassifier()

            # Set up the hyperparameter grid
            param_dist = {
                'n_estimators': [100, 200, 500],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4],
                'max_features': ['auto', 'sqrt', 'log2']
            }

            # Perform RandomizedSearchCV
            random_search = RandomizedSearchCV(
                estimator=rfc, param_distributions=param_dist, 
                n_iter=10, cv=3, verbose=2, n_jobs=-1, random_state=42
            )

            # Fit the model with the best hyperparameters
            random_search.fit(X_train, y_train)
            
            # Evaluate the best model
            best_rfc = random_search.best_estimator_
            print(f"Best Random Forest Parameters: {random_search.best_params_}")
            
            # Save the trained model and preprocessing object
            joblib.dump(best_rfc, os.path.join(self.config.root_dir, self.config.model_name))
            save_object(file_path=self.config.preprocess_path, obj=preprocess_obj)

            logging.info("Model training and hyperparameter tuning complete. Model and preprocessing pipeline saved.")

        except Exception as e:
            logging.exception(e)
            raise e

        
        
        