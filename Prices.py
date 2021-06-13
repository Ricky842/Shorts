def price(pizza_type, pizza_size, pizza_topping):
    if pizza_type == "Bbq Steak":
        type_price = 750
        if pizza_size == "Large":
            size_price = 250
        elif pizza_size == "Medium":
            size_price = 150
        elif pizza_size == "Small":
            size_price = 50
        else:
            size_price = 0
        if pizza_topping == "Pepporoni":
            topping_price = 75
        elif pizza_topping == "Cheese":
            topping_price = 65
        elif pizza_topping == "Beef":
            topping_price = 55
        elif pizza_topping == "Chicken":
            topping_price = 45
        else:
            topping_price = 0
        total_price = type_price + size_price + topping_price
        return total_price
    elif pizza_type == "Chicken Haiwaian":
        type_price = 850
        if pizza_size == "Large":
            size_price = 250
        elif pizza_size == "Medium":
            size_price = 150
        elif pizza_size == "Small":
            size_price = 50
        else:
            size_price = 0
        if pizza_topping == "Pepporoni":
            topping_price = 75
        elif pizza_topping == "Cheese":
            topping_price = 65
        elif pizza_topping == "Beef":
            topping_price = 55
        elif pizza_topping == "Chicken":
            topping_price = 45
        else:
            topping_price = 0
        total_price = type_price + size_price + topping_price
        return total_price
    elif pizza_type == "Chicken Macon Bbq":
        type_price = 950
        if pizza_size == "Large":
            size_price = 250
        elif pizza_size == "Medium":
            size_price = 150
        elif pizza_size == "Small":
            size_price = 50
        else:
            size_price = 0
        if pizza_topping == "Pepporoni":
            topping_price = 75
        elif pizza_topping == "Cheese":
            topping_price = 65
        elif pizza_topping == "Beef":
            topping_price = 55
        elif pizza_topping == "Chicken":
            topping_price = 45
        else:
            topping_price = 0
        total_price = type_price + size_price + topping_price
        return total_price
    elif pizza_type == "Veg Feast":
        type_price = 700
        if pizza_size == "Large":
            size_price = 250
        elif pizza_size == "Medium":
            size_price = 150
        elif pizza_size == "Small":
            size_price = 50
        else:
            size_price = 0
        if pizza_topping == "Pepporoni":
            topping_price = 75
        elif pizza_topping == "Cheese":
            topping_price = 65
        elif pizza_topping == "Beef":
            topping_price = 55
        elif pizza_topping == "Chicken":
            topping_price = 45
        else:
            topping_price = 0
        total_price = type_price + size_price + topping_price
        return total_price
    else:
        total_price = 0

