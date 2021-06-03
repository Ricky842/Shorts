#Build a Pizza from Scratch
#User gets to choose from a list of Pizza Names
#They then get to choose to add extra toppings and cheese
#Finally, a choice of a side - either a soda or juice
#Total cost of the order

from Questions import Questions
from Checks import topping_check, type_check, size_check

type_prompt = ["What type of Pizza do you want?\n1.BBQ Steak\n2.Chicken Haiwaian\n"
"3.Chicken Macon BBQ\n4.Veg Feast\n",]

size_prompt = ["What Size of Pizza do you want?\n1.Large\n2.Medium\n3.Small\n"]

topping_prompt = ["What toppings would you want in your Pizza?\n1.Pepporoni\n2.Cheese\n3.Beef\n4.Chicken\n"]

type_questions = [Questions(type_prompt[0], "")]

size_questions = [Questions(size_prompt[0], "")]

topping_questions = [Questions(topping_prompt[0],"")]

def pizza_check(type_questions, size_questions,topping_questions):
    for question in type_questions:
        type_answer_res = input(question.prompt)
        type_answer = type_check(type_answer_res)
    for question in size_questions:
        size_answer = input(question.prompt)
        size_answer = size_check(size_answer)
    for question in topping_questions:
        topping_answer = input(question.prompt)
        topping_answer = topping_check(topping_answer)
    print("You want a {} {} Pizza with {} toppings".format(size_answer, type_answer, topping_answer))
    
pizza_check(type_questions,size_questions,topping_questions)
