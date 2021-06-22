type = ["Bbq Steak", "Chicken Haiwaian", "Chicken Macon Bbq", "Veg Feast"]
type_prices = {"Bbq Steak":750, "Chicken Haiwaian":850, "Chicken Macon Bbq":950,"Veg Feast":700}
size = ["Large", "Medium", "Small"]
sizes_price = {"Large": 200, "Medium": 150, "Small":50}
topping = ["Pepporoni", "Cheese", "Beef", "Chicken"]
toppings_price = {"Pepporoni":75, "Cheese":65, "Beef":55, "Chicken":45}

def price(pizza_type, pizza_size, pizza_topping):
    if pizza_type in type:
        type_price = type_prices[pizza_type]
        if pizza_size in size:
            size_price = sizes_price[pizza_size]
            if pizza_topping in topping:
                topping_price = toppings_price[pizza_topping]
        total_price = type_price + size_price + topping_price
    return total_price
