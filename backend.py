import os

import openai
from dotenv import load_dotenv

load_dotenv()


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_response(self, user_input):
        return openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4080,
            temperature=0.5
        ).choices[0].text


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds")
    print(response)
