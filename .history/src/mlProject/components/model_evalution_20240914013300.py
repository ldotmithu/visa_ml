def save_result(self):
    """Evaluate the model on test data and save the accuracy score as JSON."""
    try:
        # Load the test data
        test_data = pd.read_csv(self.config.test_data_path)
        
        # Load the model and preprocessing object
        model = joblib.load(self.config.model_path)
        preprocess_obj = load_object(self.config.preprocess_path)
        
        # Prepare the test data
        target_col = 'case_status'
        X_test = test_data.drop(columns=['case_status', 'case_id', 'yr_of_estab'], axis=1)
        y_test = test_data[target_col]
        
        # Convert target values to binary format (0 = Certified, 1 = Denied)
        y_test = np.where(y_test == 'Denied', 1, 0)
        
        # Apply the preprocessing pipeline to the test data
        X_test = preprocess_obj.transform(X_test)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Convert predictions to binary format (0 = Certified, 1 = Denied)
        y_pred = np.where(y_pred == 'Denied', 1, 0)
        
        # Evaluate the model
        acc_score = self.eval_metrics(y_test, y_pred)
        logging.info(f"Model accuracy: {acc_score}")
        
        # Save the accuracy score as a JSON file
        score = {'accuracy_score': acc_score}
        save_json(Path(self.config.metric_file_path), data=score)
        
    except Exception as e:
        logging.exception("Error during model evaluation.")
        raise e
