from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)  # initializing a flask app

@app.route('/', methods=['GET', 'POST'])
def homePage():
    if request.method == 'POST':
        # Extract form data
        form_data = {
            'continent': request.form.get('continent'),
            'education_of_employee': request.form.get('education_of_employee'),
            'has_job_experience': request.form.get('has_job_experience'),
            'requires_job_training': request.form.get('requires_job_training'),
            'no_of_employees': request.form.get('no_of_employees'),
            'region_of_employment': request.form.get('region_of_employment'),
            'prevailing_wage': request.form.get('prevailing_wage'),
            'unit_of_wage': request.form.get('unit_of_wage'),
            'full_time_position': request.form.get('full_time_position')
        }
        
        # Create a DataFrame from form data
        df = pd.DataFrame([form_data])
        
        # Initialize PredictionPipeline and make predictions
        prediction_pipeline = PredictionPipeline()
        prediction_result = prediction_pipeline.predict(df)
        
        # Render the result on the HTML page
        return render_template('index.html', context=prediction_result)
    
    return render_template("index.html", context="")

@app.route('/train', methods=['GET'])
def training():
    try:
        os.system("python main.py")
        return "Training Successful!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

