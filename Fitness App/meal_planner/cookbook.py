from meal_planner.meal_planner import *

######################################
#             MyFridge               #
######################################

############# MEATS #############
one_egg = FridgeItem('Eggs (Raw)', 0.5)
chicken_breast = FridgeItem('Raw Chicken Breast', 2.72)
one_cup_ground_beef = FridgeItem('Ground Beef Raw', 2.26)
one_hotdog = FridgeItem('Frankfurter Meat', .52)
chicken_quarter = FridgeItem('Boneless Skinless Chicken Leg (Raw)', 2.65)
one_cup_ground_pork = FridgeItem('Pork Fresh Ground Raw', 2.29)

############# FRUITS #############
one_apple = FridgeItem("Apples", 1.82)
one_banana = FridgeItem("Bananas", 1.18)
one_tomato = FridgeItem('Tomatoes', 1.23)
one_cup_tomato_sauce = FridgeItem('Tomato Sauce Canned No Salt Added', 2.4)
ten_grapes = FridgeItem("Grapes", .2)
one_tangerine = FridgeItem("Tangerines", .88)
one_strawberry = FridgeItem('Strawberries', .12)
ten_blueberries = FridgeItem('Blueberries', .136)

############# VEGETABLES #############
one_pepper = FridgeItem('Green Bell Peppers', 1.19)
one_mushroom = FridgeItem('White Button Mushrooms', .18)
one_onion = FridgeItem('Onions', 1.10)
one_cup_kale = FridgeItem('Kale', .16)
one_carrot = FridgeItem('Carrots', .72)
one_celery = FridgeItem('Celery', .64)
one_garlic_clove = FridgeItem('Garlic', .03)
one_potato = FridgeItem('Potatoes Flesh And Skin Raw', 1.48)
one_cup_peas = FridgeItem('Peas', 1.45)
one_dill_pickle = FridgeItem('Dill Pickles', .35)

############# DAIRY #############
one_cup_a_milk = FridgeItem("Unsweetened Almond Milk", 2.62)
one_cup_p_g_yogurt = FridgeItem('Greek Yogurt (Plain)', 2.5)

############# CARBOHYDRATES #############
one_cup_oats = FridgeItem("Uncooked Oats", 1.6)
one_cup_flour = FridgeItem('Wheat Flour White All-Purpose Unenriched', 1.25)
one_tsp_baking_powder = FridgeItem("Leavening Agents Baking Powder Low-Sodium", .04)
one_loaf_italian_bread = FridgeItem('Bread Italian', 8)
one_cup_pasta_noodles = FridgeItem('Noodles Cooked', 1.6)
one_cup_granola = FridgeItem('Cereal Granola', .56)

############# FATS #############
one_tbsp_olive_oil = FridgeItem('Olive Oil', .14)
one_tbsp_peanut_butter = FridgeItem("Peanut Butter (Smooth)", .16)

############# OTHER #############
one_cup_coffee = FridgeItem('Coffee', 2.37)
one_tbsp_maple_syrup = FridgeItem('Syrups Maple', .2)
one_cup_chicken_broth = FridgeItem('Soup Chicken Broth Cubes Dry Prepared With Water', 2.45)
one_can_chili = FridgeItem('Canned Chili With Beans', 2.36)
one_tbsp_ketchup = FridgeItem('Ketchup', .17)
one_tbsp_honey = FridgeItem('Honey', .21)
one_cup_ap_popcorn = FridgeItem('Popcorn Air-Popped Unbuttered', .08)
one_scoop_p_powder = FridgeItem("Whey Protein Powder Isolate", .43)
one_cup_mixed_nuts = FridgeItem("Mixed Nuts Unroasted", 1.42)



######################################
#             RECIPES                #
######################################


############# BREAKFAST #############

# Omlett:
eggs = Ingredient(one_egg, 2)
peppers = Ingredient(one_pepper, .25)
mushrooms = Ingredient(one_mushroom, 2)
onions = Ingredient(one_onion, .1)
kale = Ingredient(one_cup_kale, .1)
oil = Ingredient(one_tbsp_olive_oil, .25)
omlett = Recipe("Omlett", [eggs, peppers, mushrooms, onions, kale, oil])

# Coffee:
coffee = Ingredient(one_cup_coffee, 1)
coffee_milk = Ingredient(one_cup_a_milk, .1)
coffee = Recipe("Coffee with Milk", [coffee, coffee_milk])

# Homemade Oatmeal:
oats = Ingredient(one_cup_oats, 1)
milk = Ingredient(one_cup_a_milk, .125) #1/2 cup / 4
apple = Ingredient(one_apple, .5)
oatmeal = Recipe("Homemade Oatmeal", [oats, milk, apple])

# Banana Pancakes:
banana = Ingredient(one_banana, 2)
milk = Ingredient(one_cup_a_milk, 1)
eggs = Ingredient(one_egg, 1)
oil = Ingredient(one_tbsp_olive_oil, 1)
flour = Ingredient(one_cup_flour, 1)
baking_powder = Ingredient(one_tsp_baking_powder, 1)
syrup = Ingredient(one_tbsp_maple_syrup, 2)
pancakes = Recipe("Banana Pancakes", [banana, milk, eggs, oil, flour, baking_powder, syrup], 3) # 3 servings of 4

# Breakfast Sausage:
syrup = Ingredient(one_tbsp_maple_syrup, 3)
pork = Ingredient(one_cup_ground_pork, 3.36) #1 lbs
oil = Ingredient(one_tbsp_olive_oil, .5)
breakfast_sausage = Recipe("Breakfast Sausage", [syrup, pork, oil], 12)


############# LUNCH #############

# Chicken Sandwhich:
chicken = Ingredient(chicken_breast , .2)
onions = Ingredient(one_onion, .1)
tomato = Ingredient(one_tomato, 1)
kale = Ingredient(one_cup_kale, .1)
bread = Ingredient(one_loaf_italian_bread, (2/20))
sandwhich = Recipe("Chicken Sandwhich", [chicken, onions, tomato, kale, bread])

# Vegetable Soup:
onions = Ingredient(one_onion, .1)
carrots = Ingredient(one_carrot, 1)
celery = Ingredient(one_celery, 1)
sauce = Ingredient(one_cup_tomato_sauce, 1)
garlic = Ingredient(one_garlic_clove, 4)
tomato = Ingredient(one_tomato, 1)
broth = Ingredient(one_cup_chicken_broth, 6)
potato = Ingredient(one_potato, 2)
peas = Ingredient(one_cup_peas, 1)
soup = Recipe("Vegetable Soup", [onions, carrots, celery, sauce, garlic, tomato, broth, potato, peas], 8)

# Pasta Sauce:
onions = Ingredient(one_onion, 2)
carrots = Ingredient(one_carrot, 1)
sauce = Ingredient(one_cup_tomato_sauce, 3.5)
garlic = Ingredient(one_garlic_clove, 6)
oil = Ingredient(one_tbsp_olive_oil, .2)
peppers = Ingredient(one_pepper, 1)
kale = Ingredient(one_cup_kale, .25)
beef = Ingredient(one_cup_ground_beef , 2)
pasta_sauce = Recipe("Pasta Sauce", [onions, carrots, sauce, garlic, oil, peppers, kale, beef], 8)

# Pasta Noodles
raw_noodles = Ingredient(one_cup_pasta_noodles, 8)
cooked_noodles = Recipe("Pasta Noodles", raw_noodles, 8)

# Lazy Chili Dogs
raw_dog = Ingredient(one_hotdog, 4)
chili = Ingredient(one_can_chili , (1/2))
buns = Ingredient(one_loaf_italian_bread, (4/20))
lazy_chili_dogs_rec = Recipe("Lazy Chili Dogs", [raw_dog, chili, buns], 2)


############# DINNER #############

# Winner Winner Chicken Dinner:
raw_chicken = Ingredient(chicken_quarter , 1)
oil = Ingredient(one_tbsp_olive_oil, .25)
cooked_chicken = Recipe("Quarter Chicken", [raw_chicken, oil])

# French Fries:
potato =Ingredient(one_potato, 1)
oil = Ingredient(one_tbsp_olive_oil, .25)
ketchup = Ingredient(one_tbsp_ketchup, 2.5)
fries = Recipe("French Fries", [potato, oil, ketchup])

# Homemade Hamburger:
beef = Ingredient(one_cup_ground_beef, .25)
ketchup = Ingredient(one_tbsp_ketchup, 1)
onion = Ingredient(one_onion, .1)
kale = Ingredient(one_cup_kale, .1)
bread = Ingredient(one_loaf_italian_bread, (2/20))
pickles = Ingredient(one_dill_pickle, 2)
oil = Ingredient(one_tbsp_olive_oil, .25)
burger = Recipe("Burger", [beef, ketchup, onion, kale, bread, pickles, oil])


############# SNACK #############


# Fruit Salad:
banana = Ingredient(one_banana, 1)
apple = Ingredient(one_apple, 1)
grapes = Ingredient(ten_grapes, 1)
tangerines = Ingredient(one_tangerine, 1)
fruit_salad = Recipe("Fruit Salad", [banana, apple, grapes, tangerines])

# Parfait:
yogurt = Ingredient(one_cup_p_g_yogurt, 1)
granola = Ingredient(one_cup_granola, .25)
strawberry = Ingredient(one_strawberry, 1)
blueberry = Ingredient(ten_blueberries, 1)
honey = Ingredient(one_tbsp_honey, 0.1)
parfait = Recipe("Parfait", [yogurt, granola, strawberry, blueberry, honey])

# Popcorn:
popcorn_seeds = Ingredient(one_cup_ap_popcorn, 3)
popcorn = Recipe("Air Popped Popcorn", popcorn_seeds)


############# SUPPLEMENT #############


# Energy Bars:
oats = Ingredient(one_cup_oats, 2) 
powder = Ingredient(one_scoop_p_powder, 4)
milk = Ingredient(one_cup_a_milk, .5)
pb = Ingredient(one_tbsp_peanut_butter , 5)
nuts = Ingredient(one_cup_mixed_nuts, .25)
energy_bar = Recipe("Energy Bar", [oats, powder, milk, pb, nuts], 4)

# Watered Down Milk Substitute:
milk = Ingredient(one_cup_a_milk, .25)
watered_milk = Recipe("Cup of Almond Milk", milk)

# Protein Drink:
milk = Ingredient(one_cup_a_milk, .25)
ppowder = Ingredient(one_scoop_p_powder, 1)
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
