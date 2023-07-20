import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")



@app.route("/", methods=("GET", "POST"))
def index():
    """ get the prompt from the user and return the result"""
    if request.method == "POST":
        question = request.form["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0.6,
            max_tokens=100
        )
        return redirect(url_for("index", result=response.choices[0].text))
    result = request.args.get("result")
    return render_template("index.html", result=result)



@app.route("/models", methods=["GET"])
def models():
    """ return a list of models """
    available_models = openai.Model.list()
    model_names = [model['id'] for model in available_models['data']]
    return render_template("models.html", models=model_names)