pizza_name = ['BBQ Steak', 'Chicken Haiwaian',
              'Chicken Macon BBQ', 'Veg Feast']
size_pizza = ["Large", "Small", "Medium"]

def type_check(pizza_type):
    if pizza_type in pizza_type:
        print("Your choice of {} has been selected". format(pizza_type))
    else:
        print("Your selection is not on the list")
    return pizza_type

def size_check(pizza_size):
    if pizza_size in size_pizza:
        print("Your choice of {} has been selected".format(pizza_size))
    else:
        print("Your size selection is not available")
    return pizza_size
