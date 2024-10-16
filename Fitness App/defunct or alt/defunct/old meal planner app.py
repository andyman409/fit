##omlett = [('1 Chicken Egg', 2),
##          ('1 Red Bell Pepper', .25),
##          ('1 White Button Mushroom', 2),
##          ('1 Medium Onion', .25),
##          ('1 Cup Kale', .25)]
##
##def recipe_builder():
##    recipe = []
##    num_ing = int(input("Enter Number of Ingredients: "))
##    for i in range(num_ing):
##        ing = str(input("Enter Ingredient #"+str(i + 1)+": "))
##        quant = float(input("Enter Quantity of Ingredient #"+str(i + 1)+": "))
##        recipe.append((ing, quant))
##    return recipe
##
##def get_ing_macro(ing, macro):
##    return ingdf[macro][ing]
##
##def recipe_macro_calculator(recipe, macro):
##    total = 0
##    for ing in recipe:
##        ing_name = ing[0]
##        quant = ing[1]
##        total += (get_ing_macro(ing_name, macro) * quant)
##    return total
##
##def get_all_calorie_macros(recipe):
##    return {"calories" : recipe_macro_calculator(recipe, "calories"),
##            "cals_proteins" : recipe_macro_calculator(recipe, "cals_proteins"),
##            "cals_carbs" : recipe_macro_calculator(recipe, "cals_carbs"),
##            "cals_fats" : recipe_macro_calculator(recipe, "cals_fats")}
##
##print(omlett)
##print(get_ing_macro('1 Chicken Egg', "calories"))
##print(recipe_macro_calculator(omlett, "calories"))
##print(get_all_calorie_macros(omlett))
























##        if day == "Monday":
##            self.monday.add_meal(meal)
##        elif day == "Tuesday":
##            self.tuesday.add_meal(meal)
##        elif day == "Wednesday":
##            self.wednesday.add_meal(meal)
##        elif day == "Thursday":
##            self.thursday.add_meal(meal)  
##        elif day == "Friday":
##            self.friday.add_meal(meal)
##        elif day == "Saturday":
##            self.saturday.add_meal(meal)
##        elif day == "Sunday":
##            self.sunday.add_meal(meal)

##self.monday = MealScheduleDay("Monday")
##        self.tuesday = MealScheduleDay("Tuesday")
##        self.wednesday = MealScheduleDay("Wednesday")
##        self.thursday = MealScheduleDay("Thursday")
##        self.friday = MealScheduleDay("Friday")
##        self.saturday = MealScheduleDay("Saturday")
##        self.sunday = MealScheduleDay("Sunday")
##        self.schedule = {"Monday" : self.monday,
##                         "Tuesday" : self.tuesday,
##                         "Wednesday" : self.wednesday,
##                         "Thursday" : self.thursday,
##                         "Friday" : self.friday,
##                         "Saturday" : self.saturday,
##                         "Sunday" : self.sunday}
