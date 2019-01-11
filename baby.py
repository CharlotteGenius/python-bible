# the baby will keep asking until you say "just because"

from random import choice

# in this way, choice() function can be used below
# or use:
# import random
# then,    random.choice()   will be the function to use


questions = ["Why is the sky blue?:", "What are the butterflies?:", "Where are the dinosaurs?:"]
question = choice(questions)
# to randomly choose a question from the list
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?:").strip().lower()
print("Oh...Okay")
