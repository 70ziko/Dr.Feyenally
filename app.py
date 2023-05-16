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
    response = openai.Completion.create(
        engine = "davinci",
        prompt = user_text,
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
    return "Thank you for completing the survey!"


if __name__ == "__main__":
    app.run(debug=True)