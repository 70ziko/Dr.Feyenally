from flask import Flask, render_template, request, jsonify
import openai
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize Flask app
app = Flask(__name__)

# Define home route
@app.route('/')
def home():
    return render_template('index.html')

# Define chatbot route
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get user input from request
    input_text = request.form['chat-form']

    # Call OpenAI API to generate response
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract response text from API response
    response_text = response.choices[0].text.strip()

    # Return response as JSON
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)