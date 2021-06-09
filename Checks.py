pizza_name = ['BBQ Steak', 'Chicken Haiwaian',
              'Chicken Macon BBQ', 'Veg Feast']
size_pizza = ["Large", "Small", "Medium"]
topping_pizza = ['Pepporoni', 'Cheese', 'Beef', 'Chicken']

def type_check(pizza_type):
    if pizza_type == "1":
        pizza_type = "BBQ Steak"
    elif pizza_type == "2":
        pizza_type = "Chicken Haiwaian"
    elif pizza_type == "3":
        pizza_type = "Chicken Macon BBQ"
    elif pizza_type == "4":
        pizza_type = "Veg Feast"
    else:
        return pizza_type
    while pizza_type not in pizza_name:
        pizza_type = input("Please choose the appropriate type from the list: ")
    print("Your choice of {} has been selected". format(pizza_type))
    return pizza_type

def size_check(pizza_size):
    if pizza_size == "1":
        pizza_size = "Large"
    elif pizza_size == "2":
        pizza_size = "Medium"
    elif pizza_size == "3":
        pizza_size = "Small"
    else:
        return pizza_size
    while pizza_size not in size_pizza:
        pizza_size = input("Please choose the appropriate size from the list above: ")
    print("Your choice of {} has been selected".format(pizza_size))
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
    else:
        return pizza_topping
    while pizza_topping not in topping_pizza:
        pizza_topping = input("Please select the appropriate topping from the list above: ")
    print("You have added a {} topping to your Pizza!!".format(pizza_topping))
    return pizza_topping