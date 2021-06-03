#Build a Pizza from Scratch
#User gets to choose from a list of Pizza Names
#They then get to choose to add extra toppings and cheese
#Finally, a choice of a side - either a soda or juice
#Total cost of the order

from Questions import Questions
from Checks import type_check, size_check

type_prompt = [
    "What type of Pizza do you want?\n1.BBQ Steak\n2.Chicken Haiwaian\n3.Chicken Macon BBQ\n4.Veg Feast\n",
]

size_prompt = ["What Size of Pizza do you want?\n1.Large\n2.Medium\n3.Small\n"]

type_questions = [
    Questions(type_prompt[0], "")
]

size_questions = [
    Questions(size_prompt[0], "")
]

def pizza_check(type_questions, size_questions):
    for question in type_questions:
        type_answer = input(question.prompt)
        type_answer = type_check(type_answer)
    for question in size_questions:
        size_answer = input(question.prompt)
        size_answer = size_check(size_answer)
    print("You want a {} {} Pizza".format(size_answer, type_answer))
    
pizza_check(type_questions,size_questions)
