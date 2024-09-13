from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homePage():
        return render_template("index.html")

    @app.route('/train', methods=['GET'])
    def training():
        os.system("python main.py")
        return "Training Successful!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8080)
