from flask import Flask, render_template, request, redirect, url_for
from us_visa.pipline.prediction_pipeline import USvisaData, USvisaClassifier
from us_visa.pipline.training_pipeline import TrainPipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Collect data from form
            continent = request.form.get("continent")
            education_of_employee = request.form.get("education_of_employee")
            has_job_experience = request.form.get("has_job_experience")
            requires_job_training = request.form.get("requires_job_training")
            no_of_employees = request.form.get("no_of_employees")
            company_age = request.form.get("company_age")
            region_of_employment = request.form.get("region_of_employment")
            prevailing_wage = request.form.get("prevailing_wage")
            unit_of_wage = request.form.get("unit_of_wage")
            full_time_position = request.form.get("full_time_position")
            
            # Create instance of USvisaData
            usvisa_data = USvisaData(
                continent=continent,
                education_of_employee=education_of_employee,
                has_job_experience=has_job_experience,
                requires_job_training=requires_job_training,
                no_of_employees=no_of_employees,
                company_age=company_age,
                region_of_employment=region_of_employment,
                prevailing_wage=prevailing_wage,
                unit_of_wage=unit_of_wage,
                full_time_position=full_time_position,
            )
            
            usvisa_df = usvisa_data.get_usvisa_input_data_frame()
            model_predictor = USvisaClassifier()
            value = model_predictor.predict(dataframe=usvisa_df)[0]
            status = "Visa-approved" if value == 1 else "Visa Not-Approved"
            
            return render_template("usvisa.html", context=status)
        
        except Exception as e:
            return f"Error Occurred: {e}"

    return render_template("usvisa.html", context="Rendering")

@app.route("/train")
def train_route_client():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return "Training successful !!"
    except Exception as e:
        return f"Error Occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
