from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=['POST'])
def get_bot_response():
    data = request.get_json()
    messages = data["messages"]
    print(messages)
    # user_text = messages[-1]["content"]
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        max_tokens = 200,
        n = 1,
        presence_penalty = 0,
        frequency_penalty = 0,
        stop = None,
        temperature = 0.8,
    )

    # Extract response text from API response
    response = response.choices[0].message.content.strip()
    return str(response)

@app.route("/survey", methods=["POST"])
def receive_survey():

    survey_responses = request.form.getlist('response[]')

    # Process the survey responses as needed
    # ...

    # Return a response to the client
    return "Dziękuję za wypełnienie ankiety!"


if __name__ == "__main__":
    app.run(debug=True)