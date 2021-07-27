pizza_name = ['Bbq Steak', 'Chicken Haiwaian',
              'Chicken Macon Bbq', 'Veg Feast']
size_pizza = ["Large", "Small", "Medium"]
topping_pizza = ['Pepporoni', 'Cheese', 'Beef', 'Chicken']

def type_check(pizza_type):
    if pizza_type == "1":
        pizza_type = "Bbq Steak"
    elif pizza_type == "2":
        pizza_type = "Chicken Haiwaian"
    elif pizza_type == "3":
        pizza_type = "Chicken Macon Bbq"
    elif pizza_type == "4":
        pizza_type = "Veg Feast"
    while pizza_type not in pizza_name:
        pizza_type_ret = input("Please choose the appropriate type from the list: ").title()
        pizza_type = type_check(pizza_type_ret)
        return pizza_type
    print(f"Your choice of {pizza_type} has been selected")
    return pizza_type

def size_check(pizza_size):
    if pizza_size == "1":
        pizza_size = "Large"
    elif pizza_size == "2":
        pizza_size = "Medium"
    elif pizza_size == "3":
        pizza_size = "Small"
    while pizza_size not in size_pizza:
        pizza_size_ret = input("Please choose the appropriate size from the list above: ").title()
        pizza_size = size_check(pizza_size_ret)
        return pizza_size
    print(f"Your choice of {pizza_size} has been selected")
    return pizza_size

def topping_check(pizza_topping):
    if pizza_topping == "1":
        pizza_topping = "Pepporoni"
    elif pizza_topping == "2":
        pizza_topping = "Cheese"
    elif pizza_topping == "3":
        pizza_topping = "Beef"
    elif pizza_topping == "4":
        pizza_topping = "Chicken"
    while pizza_topping not in topping_pizza:
        pizza_topping_ret = input("Please select the appropriate topping from the list above: ").title()
        pizza_topping = topping_check(pizza_topping_ret)
        return pizza_topping
    print(f"You have added a {pizza_topping} topping to your Pizza!!")
    return pizza_topping