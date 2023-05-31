from flask import Flask, render_template, request
import openai
import os
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

parameters = {
    "engine": "gpt-3.5-turbo",
    "max_tokens": 60,
    "temperature": 0.8,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": ["\n", " Human:", " AI:"]
}

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "system", "content": "You are an AI designed to help people fill out surveys and answer questions related to ophthalmology. You specialize in ophthalmology surveys and helping people answer questions about eye problems. You are very good at your job. You are friendly and helpful."},
                    { "role": "user", "content": user_text}],
        max_tokens = 60,
        n = 1,
        presence_penalty = 0,
        frequency_penalty = 0,
        top_p = 1,
        stop = None,
        temperature = 0.8,
    )

    # Extract response text from API response
    response_text = response.choices[0].text.strip()

    return str(response_text)

@app.route("/survey", methods=["POST"])
def receive_survey():

    survey_responses = request.form.getlist('response[]')

    # Process the survey responses as needed
    # ...

    # Return a response to the client
    return "Dziękuję za wypełnienie ankiety!"

def receive_messages():
    pass


if __name__ == "__main__":
    app.run(debug=True)