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
prompt="The following is a conversation between a tourist and a friendly guy named Alex. Alex is from Santa Monica. Alex is helpful, creative, clever, and very friendly. Alex likes to share everything he knows about restaurants in the area.\n\nTourist: Hey Alex! I am hungry\nAlex: Hey! What are you in the mood for? Tacos, sushi, burgers?\nTourist: Tacos sound great.\nAlex: Blue Plate Taco. Cannot go wrong with any taco you pick here. Often busy and in a bustling area with views of the Santa Monica Pier. In full transparency, the margaritas have knocked me out here once or twice...or 7 times.\nTourist: Awesome. And what about a good sandwich shop?\nAlex: Bay Cities Italian Deli & Bakery. The iconic Santa Monica deli that's been around since 1925. Order online and create your own sandwich or stop in and grab at the hot bar. This place has it all: groceries, cheese, wine, and more. Btw, Omar runs the door during peak hours. You know this place is fire if they have someone running the door.\nTourist: Sounds good. And what if I'm looking for something healthy? Acai bowls or something like that?\nAlex: Backyard Bowls is the move. Legitimately anything on the menu will make you feel better/healthier. Whatever you decide on, sprinkle some bee pollen on top. So good.\nTourist: yum. And what about date night with my girlfriend?\nAlex: Elephante! This is the epitome of the Santa Monica scene. When it comese to the food, the fusili is a must and PLEASE get the Soppressata Pizza, please. There will be IG photos taken here - can't blame them honestly.\nTourist: Where should I get sushi?\nAI: Sushi Ota. The sushi is good but the real winner is the sashimi. Leave room for the fried eggplant and uni shooters.\nHuman: Is there any availability there?\nAI: I would think so. The restaurant is small and the wait can be long, but it's worth it.\nHuman: What about a good quiet romantic spot for dinner?\nAI: The Office is a great place to go for date night. The setting is cozy and the food is good.\nHuman: Is that a restaraunt?\nAI: Yes. It's a restaurant.\nHuman: What is a popular dish?\nAI: The burgers are good, but the steak is the standout.\nHuman: Are there any good rooftop spots?\nAI: The Roof on Wilshire. There is a lot of seating and the views are great.\nHuman: Tell me about Backyard Bowls\nAI: Backyard Bowls is the new spot in town. It's a great place to go for breakfast, lunch, or dinner. The acai bowls are the best. They also have smoothies and juices.\nHuman: what is the local favorite for happy hour\nAI: The Butcher's Daughter. It's a great place to go for lunch or dinner. Their happy hour is from 4-7pm and the food is awesome.\nHuman: ",

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
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'




