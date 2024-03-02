spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
    #for food in spicy_foods:
     #print(food["name"])
    pass

def get_spiciest_foods(spicy_foods):
    spiciest_foods_list = []
    for food in spicy_foods:
        if isinstance(food, dict) and food.get("heat_level", 0) > 5:
         spiciest_foods_list.append(food)
    return spiciest_foods_list
    spiciest_list = get_spiciest_foods(spicy_foods)
    print(spiciest_list)

    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        

        heat_emojis = "🌶" * heat_level
        
        
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")
    #print_spicy_foods(spicy_foods)
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

american_spicy_food = get_spicy_food_by_cuisine(spicy_foods, "American")
print(american_spicy_food)

pass


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            
            #creating the emojis
            heat_emojis = "🌶" * heat_level
            
            # printing the information on spicyy food 
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")
            
    pass

    
#def average_heat_level(spicy_foods):


def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)

    if num_spicy_foods == 0:
        return 0

    average_heat_level = total_heat_level / num_spicy_foods
    print(f"Average Heat Level: {average_heat_level}")

    return average_heat_level


    


def create_spicy_food(spicy_foods, new_spicy_food):
    if not isinstance(new_spicy_food, dict):
        print("new_spicy_food should be a dictionary.")
        return spicy_foods

    required_keys = {"name", "cuisine", "heat_level"}
    if not required_keys.issubset(new_spicy_food.keys()):
        print("new_spicy_food must contain 'name', 'cuisine', and 'heat_level'.")
        return spicy_foods

    spicy_foods.append(new_spicy_food)
    print(f"Spicy food added")
    
    return spicy_foods



