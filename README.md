# Dr. Feyenally - opthology best chatbot

This is a chatbot web application built using Flask and powered by OpenAI. It allows users to have interactive conversations with the chatbot and also includes a survey feature.

## Features

- Interactive conversation with the chatbot
- Conducting a survey within the chatbot
- Seamless integration with the OpenAI API for generating chatbot responses

## Getting Started

To run the chatbot web app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/70ziko/Dr.Feyenally.git
   cd chatbot-web-app

Install the dependencies:

    pip install -r requirements.txt

Set the OpenAI API key as an environment variable:

    export OPENAI_API_KEY=<your-api-key>

Run the application:

    flask run
    or
    python app.py

Open your web browser and visit http://localhost:5000 to access the chatbot web app.

## Usage

    Upon accessing the web app, you will see the chat interface with a welcome message from the chatbot.
    Type your message in the input box and press Enter or click the Send button to send your message to the chatbot.
    The chatbot will respond with its generated response based on the OpenAI API.
    To initiate the survey, type "start survey" in the input box or click the "Start Survey" button.
    Answer the survey questions one by one by typing your responses in the chatbox.
    Once you have finished answering the survey questions, type "end survey" to conclude the survey.
    The survey responses will be processed and stored by the server (you can customize this logic in the app.py file).
    After completing the survey, you can continue having a conversation with the chatbot.

## Customization

    You can modify the chatbot's behavior and responses by adjusting the parameters and logic in the getResponse() function in the index.html file.
    For advanced customization of the chatbot's responses, you can modify the OpenAI API call and parameters in the app.py file.

## License

This project is licensed under the MIT License.

Feel free to modify and adapt the code to suit your needs. Contributions are also welcome!
