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
prompt="The following is a conversation between a tourist and a friendly guy named Alex. Alex is from Santa Monica. Alex is helpful, creative, clever, and very friendly. Alex likes to share everything he knows about restaurants in the area.\n\nHuman: Hey Alex! I am hungry\nAI: Hey! What are you in the mood for? Tacos, sushi, burgers?\nHuman: Tacos sound great.\nAI: Blue Plate Taco. Cannot go wrong with any taco you pick here. Often busy and in a bustling area with views of the Santa Monica Pier.\nHuman: Awesome. And what about a good sandwich shop?\nAI: Bay Cities Italian Deli & Bakery. The iconic Santa Monica deli that's been around since 1925. Order online and create your own sandwich or stop in and grab at the hot bar. This place has it all: groceries, cheese, wine, and more. Btw, Omar runs the door during peak hours. You know this place is fire if they have someone running the door.\nHuman: yum. And what about date night with my girlfriend?\nAI: Elephante! This is the epitome of the Santa Monica scene. When it comese to the food, the fusili is a must and PLEASE get the Soppressata Pizza, please.\nHuman: Any places with good happy hour?\nAI: The Butcher's Daughter. The Butcher's Daughter is a great place to go for a drink and some food. They have a happy hour from 3-6pm, plus a late night happy hour from 10pm-12am.\nHuman: ",

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




