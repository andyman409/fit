from meal_planner import Ingredient, Recipe, Meal


######################################
#             RECIPES                #
######################################


############# BREAKFAST #############

# Omlett:
eggs = Ingredient('1 Chicken Egg', 2)
peppers = Ingredient('1 Red Bell Pepper', .25)
mushrooms = Ingredient('1 White Button Mushroom', 2)
onions = Ingredient('1 Medium Onion', .1)
kale = Ingredient('1 Cup Kale', .1)
oil = Ingredient('1 Tbsp Extra Virgin Olive Oil', .25)
omlett = Recipe("Omlett", [eggs, peppers, mushrooms, onions, kale, oil])

# Coffee:
coffee = Ingredient('1 Cup Coffee', 1)
coffee_milk = Ingredient("1 Cup Almond Milk", .1) #1/10 of a cup
coffee = Recipe("Coffee with Milk", [coffee, coffee_milk])

# Homemade Oatmeal:
oats = Ingredient("1/2 Cup Steel Cut Oatmeal (Bob's Red Mill)", 1)
milk = Ingredient("1 Cup Almond Milk", .125) #1/2 cup / 4
apple = Ingredient("1 Medium Apple", .5)
oatmeal = Recipe("Homemade Oatmeal", [oats, milk, apple])

# Banana Pancakes:
banana = Ingredient("1 Medium Banana", 2)
milk = Ingredient("1 Cup Almond Milk", 1)
eggs = Ingredient('1 Chicken Egg', 1)
oil = Ingredient('1 Tbsp Extra Virgin Olive Oil', 1)
flour = Ingredient('1 Cup All Purpose Flour', 1)
baking_powder = Ingredient('1 Tsp Baking Powder', 1)
syrup = Ingredient('1 Tbsp Maple Syrup', 2)
pancakes = Recipe("Banana Pancakes", [banana, milk, eggs, oil, flour, baking_powder, syrup], 3) # 3 servings of 4


############# LUNCH #############

# Chicken Sandwhich:
chicken = Ingredient('1 Chicken Breast (Skinless)', .2)
onions = Ingredient('1 Medium Onion', .1)
tomato = Ingredient('1 Medium Tomato', 1)
kale = Ingredient('1 Cup Kale', .1)
bread = Ingredient('1 Baguette', (1/5))
sandwhich = Recipe("Chicken Sandwhich", [chicken, onions, tomato, kale, bread])

# Vegetable Soup:
onions = Ingredient('1 Medium Onion', .1)
carrots = Ingredient('1 Large Carrot', 1)
celery = Ingredient('1 Large Celery Stalk', 1)
sauce = Ingredient('1 Cup Plain Tomato Sauce', 1)
garlic = Ingredient('1 Garlic Clove', 4)
tomato = Ingredient('1 Medium Tomato', 1)
broth = Ingredient('1 Cup Chicken Broth', 6)
potato = Ingredient('1 Potato', 2)
peas = Ingredient('1 Cup Peas', 1)
soup = Recipe("Vegetable Soup", [onions, carrots, celery, sauce, garlic, tomato, broth, potato, peas], 8)

# Pasta Sauce:
onions = Ingredient('1 Medium Onion', 2)
carrots = Ingredient('1 Large Carrot', 1)
sauce = Ingredient('1 Cup Plain Tomato Sauce', 3.5)
garlic = Ingredient('1 Garlic Clove', 6)
oil = Ingredient('1 Tbsp Extra Virgin Olive Oil', .2)
peppers = Ingredient('1 Red Bell Pepper', 1)
kale = Ingredient('1 Cup Kale', .25)
beef = Ingredient('1 Cup Raw Ground Beef', 2)
pasta_sauce = Recipe("Pasta Sauce", [onions, carrots, sauce, garlic, oil, peppers, kale, beef], 8)

# Pasta Noodles
raw_noodles = Ingredient('1 Cup Pasta Noodles', 8)
cooked_noodles = Recipe("Pasta Noodles", raw_noodles, 8)

# Lazy Chili Dogs
raw_dog = Ingredient('1 Frankfurter', 4)
chili = Ingredient('1 Can Tim Hortons Homestyle Chili', (1/2))
buns = Ingredient('1 Baguette', (2/5))
lazy_chili_dogs_rec = Recipe("Lazy Chili Dogs", [raw_dog, chili, buns], 2)


############# DINNER #############

# Winner Winner Chicken Dinner:
raw_chicken = Ingredient('1 Chicken Leg Quarter (Skinless)', 1)
oil = Ingredient('1 Tbsp Extra Virgin Olive Oil', .25)
cooked_chicken = Recipe("Quarter Chicken", [raw_chicken, oil])

# French Fries:
potato =Ingredient('1 Potato', 1)
oil = Ingredient('1 Tbsp Extra Virgin Olive Oil', .25)
ketchup = Ingredient('1 Tbsp Ketchup', 2.5)
fries = Recipe("French Fries", [potato, oil, ketchup])

# Homemade Hamburger:
beef = Ingredient('1 Cup Raw Ground Beef', .25)
ketchup = Ingredient('1 Tbsp Ketchup', 1)
onion = Ingredient('1 Medium Onion', .1)
kale = Ingredient('1 Cup Kale', .1)
bread = Ingredient('1 Baguette', (1/5))
pickles = Ingredient('1 Pickled Cucumber', 1)
oil = Ingredient('1 Tbsp Extra Virgin Olive Oil', .25)
burger = Recipe("Burger", [beef, ketchup, onion, kale, bread, pickles, oil])


############# SNACK #############


# Fruit Salad:
banana = Ingredient("1 Medium Banana", 1)
apple = Ingredient("1 Medium Apple", 1)
grapes = Ingredient("10 Grapes", 1)
tangerines = Ingredient("1 Tangerine", 1)
fruit_salad = Recipe("Fruit Salad", [banana, apple, grapes, tangerines])

# Parfait:
yogurt = Ingredient('1 Cup Plain Greek Yogurt', .75)
granola = Ingredient('1 Cup Harvest Crunch Granola Cereal', .25)
strawberry = Ingredient('1 Large Strawberry', 1)
blueberry = Ingredient('1 Blueberry', 10)
honey = Ingredient('1 Tbsp Honey', 0.1)
parfait = Recipe("Parfait", [yogurt, granola, strawberry, blueberry, honey])

# Popcorn:
popcorn_seeds = Ingredient('1 Cup Air Popped Popcorn', 3)
popcorn = Recipe("Air Popped Popcorn", popcorn_seeds)


############# SUPPLEMENT #############


# Energy Bars:
oats = Ingredient("1/2 Cup Steel Cut Oatmeal (Bob's Red Mill)", 2) 
powder = Ingredient("1 Scoop Pure Protein Whey Protein Powder", 4)
milk = Ingredient("1 Cup Almond Milk", .5)
pb = Ingredient("1 Tbsp Peanut Butter", 5)
nuts = Ingredient("1 oz Mixed Nuts", 4)
energy_bar = Recipe("Energy Bar", [oats, powder, milk, pb, nuts], 4)

# Watered Down Milk Substitute:
milk = Ingredient("1 Cup Almond Milk", .25)
watered_milk = Recipe("Cup of Almond Milk", milk)

# Protein Drink:
milk = Ingredient("1 Cup Almond Milk", .25)
ppowder = Ingredient("1 Scoop Pure Protein Whey Protein Powder", 1)
protein_drink_rec = Recipe("Protein Drink", [milk, ppowder])



######################################
#             MEALS                  #
######################################


############# BREAKFAST #############

omlett_breakfast = Meal("Omlett Breakfast", "Breakfast", [omlett, coffee])
oatmeal_meal = Meal("Homemade Oatmeal", "Breakfast", [oatmeal, coffee])
pancake_breakfast = Meal("Banana Pancake Breakfast", "Breakfast", [pancakes, coffee])


############# LUNCH #############

soup_and_sandwhich = Meal("Soup and Sandwhich", "Lunch", [soup, sandwhich])
pasta = Meal("Pasta", "Lunch", [pasta_sauce, cooked_noodles])
lazy_chili_dogs = Meal("Lazy Chili Dogs", "Lunch", lazy_chili_dogs_rec)

############# DINNER #############

chicken_dinner = Meal("Winner Winner Chicken Dinner", "Dinner", [cooked_chicken, fries])
burger_dinner = Meal("Homemade Hamburger Dinner", "Dinner", [burger, fries])


############# SNACK #############

fruit_salad_snack = Meal("Fruit Salad", "Snack", fruit_salad)
parfait_snack = Meal("Parfait", "Snack", parfait)
popcorn_snack = Meal("Air Popped Popcorn", "Snack", popcorn)


############# SUPPLEMENT #############

energy_bar = Meal("Energy Bar with Almond Milk", "Supplement", [energy_bar, watered_milk])
protein_drink = Meal("Protein Drink", "Supplement", protein_drink_rec)




############# GLOBAL VARIABLE #############

meal_list = [omlett_breakfast, oatmeal_meal, pancake_breakfast,
             soup_and_sandwhich, pasta, lazy_chili_dogs,
             chicken_dinner, burger_dinner,
             fruit_salad_snack, popcorn_snack, parfait_snack,
             energy_bar, protein_drink]
