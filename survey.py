from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Define conversation flow using the survey questions and possible answers
survey = [
    {
        'question': 'Do your eyes hurt?',
        'answers': ['1. No / Nie', '2. Yes: burning / pieczenie', '3. Yes: itching / swędzenie', '4. Yes: pain / ból']
    },
    {
        'question': 'Do you wear glasses?',
        'answers': ['1. No / Nie', '2. Yes: krótkowzroczność', '3. Tak: dalekowzroczność']
    },
    {
        'question': 'Do you have any eye disorders?',
        'answers': ['1. No / Nie', '2. Yes: astygmatyzm', '3. Yes: zaćma', '4. Yes: jaskra', '5. Yes: inne']
    },
    {
        'question': 'Are you taking eye medications?',
        'answers': ['1. No / Nie']
    },
    {
        'question': 'Do you have allergies?',
        'answers': ['1. No / Nie']
    },
    {
        'question': 'Do you have photophobia?',
        'answers': ['1. No / Nie']
    },
    {
        'question': 'Do you have symptoms of a dry eye?',
        'answers': ['1. No / Nie']
    }
]

# Create a new chatbot
bot = ChatBot('Eye Survey Bot')

# Train the chatbot with the survey questions and possible answers
trainer = ChatterBotCorpusTrainer(bot)
trainer.train(survey)

# Conduct the survey
for question in survey:
    print(question['question'])
    for answer in question['answers']:
        print(answer)
    user_input = input('> ')
    bot_input = ' '.join(user_input.split()[1:])  # Remove the number prefix from the user's answer
    bot_response = bot.get_response(bot_input)
    print(bot_response)