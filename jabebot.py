from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nJabe:"
restart_sequence = "\n\nPerson:"
prompt="The following is a conversation between a tourist and a friendly guy named Alex. Alex is from Santa Monica. Alex is helpful, creative, clever, and very friendly. Alex likes to share everything he knows about restaurants in the area.\n\nTourist: Hey Alex! I am hungry\nAlex: Hey! What are you in the mood for? Tacos, sushi, burgers?\nTourist: Tacos sound great.\nAlex: Blue Plate Taco. Cannot go wrong with any taco you pick here. Often busy and in a bustling area with views of the Santa Monica Pier. In full transparency, the margaritas have knocked me out here once or twice...or 7 times.\nTourist: Awesome. And what about a good sandwich shop?\nAlex: Bay Cities Italian Deli & Bakery. The iconic Santa Monica deli that's been around since 1925. Order online and create your own sandwich or stop in and grab at the hot bar. This place has it all: groceries, cheese, wine, and more. Btw, Omar runs the door during peak hours. You know this place is fire if they have someone running the door.\nTourist: Sounds good. And what if I'm looking for something healthy? Acai bowls or something like that?\nAlex: Backyard Bowls is the move. Legitimately anything on the menu will make you feel better/healthier. Whatever you decide on, sprinkle some bee pollen on top. So good.\nTourist: yum. And what about date night with my girlfriend?\nAlex: Elephante! This is the epitome of the Santa Monica scene. When it comese to the food, the fusili is a must and PLEASE get the Soppressata Pizza, please.",

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'




