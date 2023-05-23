from flask import Flask, render_template, request
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        prompt = user_text,
        messages = [],
        max_tokens = 60,
        n = 1,
        stop = None,
        temperature = 0.7,
    )

    response_text = response.choices[0].text.strip()

    return str(response_text)

@app.route("/survey", methods=["POST"])
def receive_survey():

    survey_responses = request.form.getlist('response[]')

    # Process the survey responses as needed
    # ...

    # Return a response to the client
    return "Dziękuję za wypełnienie ankiety!"


if __name__ == "__main__":
    app.run(debug=True)