import pandas as pd

######################################
#          Meal Planner              #
######################################


######## GENERAL FUNCTIONS & GLOBAL VARIABLES ########


ingdf = pd.read_excel(r"C:\Users\andys\Desktop\Meal Planning\meal_planner_data.xlsx",
                   sheet_name="Ingredients",
                   index_col="food_name",
                   converters={"food_name" : str,
                               "food_type" : str,
                               "grams" : float,
                               "grams_proteins" : float,
                               "grams_carbs" : float,
                               "grams_fats" : float,
                               "calories" : float,
                               "cals_proteins" : float,
                               "cals_carbs" : float,
                               "cals_fats" : float})

full_macros = ["grams", "grams_proteins", "grams_carbs", "grams_fats",
          "calories", "cals_proteins", "cals_carbs", "cals_fats"]

macros = ["calories", "cals_carbs", "cals_fats", "cals_proteins"]

meal_types = ["Breakfast", "Lunch", "Dinner", "Snack", "Supplement"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday"]

def macro_name_converter(macro):
    if macro == "calories":
        return "Total Calories"
    elif macro == "cals_carbs":
        return "Calories from Carbohydrates"
    elif macro == "cals_fats":
        return "Calories from Fats"
    elif macro == "cals_proteins":
        return "Calories from Proteins"
    

######## CLASSES ########

class Ingredient():
    def __init__(self, name, quantity):
        '''
        name: Str
        quantity: Float
        '''
        self.name = name
        self.quantity = quantity
        
    def get_macro(self, macro):
        '''
        macro: Str in macros global variable
        '''
        return (ingdf[macro][self.name] * self.quantity)
    
    def show_macros(self):
        print(self.name + " x " + str(self.quantity) + " has the following Macros:")
        for macro in macros:
            print("    " + macro + ": " + str(round(self.get_macro(macro), 2)))

class Recipe():
    def __init__(self, name, ingredients=None, servings=1):
        '''
        ingredients: Ingredient or List of Ingredients (Optional)
        servings: Int (Optional). Default is 1
        '''
        self.name = name
        self.servings = servings
        self.ingredients = []
        if isinstance(ingredients, Ingredient):
            self.ingredients.append(ingredients)
        elif isinstance(ingredients, list):
            self.ingredients.extend(ingredients)

    def add_ingredients(self, ingredients):
        '''
        ingredients: Ingredient or List of Ingredients
        '''
        if isinstance(ingredients, Ingredient):
            self.ingredients.append(ingredients)
        elif isinstance(ingredients, list):
            self.ingredients.extend(ingredients)
    
    def get_macro(self, macro, servings=1):
        '''
        macro: Str in global variables macros
        servings: Int (Optional). Default is 1

        Returns the quantity of the macro contained in a number of servings. Default is 1 serving.
        '''
        total = 0
        for ingredient in self.ingredients:
            total += ((ingredient.get_macro(macro) / self.servings) * servings) # double check math
        return total

    def show_macros(self):
        print("1 " + self.name + " has the following Macros:")
        for macro in macros:       
            print("    " + macro + ": " + str(round(self.get_macro(macro), 2)))

class Meal():
    '''
    Represents 1 serving of a meal constructed from 1 or more Recipes
    '''
    def __init__(self, meal_name, meal_type, recipes=None):
        '''
        meal_name: Str
        meal_type: Str
        recipes: either Recipe or List of Recipe
        '''
        self.meal_name = meal_name
        self.meal_type = meal_type
        self.recipes = []
        if isinstance(recipes, Recipe):
            self.recipes.append(recipes)
        elif isinstance(recipes, list):
            self.recipes.extend(recipes)

    def add_recipes(self, recipes):
        '''
        recipes: either Recipe or List of Recipe
        '''
        if isinstance(recipes, Recipe):
            self.recipes.append(recipes)
        elif isinstance(recipes, list):
            self.recipes.extend(recipes)

    def get_macro(self, macro):
        total = 0
        for recipe in self.recipes:
            total += recipe.get_macro(macro)
        return total

    def show_recipes(self):
        print(self.meal_name + " includes the following Recipes:")
        for recipe in self.recipes:
            print("- " + recipe.name)

    def show_macros(self):
        print(self.meal_name + " has the following Macros:")
        for macro in macros:
            print("    " + macro + ": " + str(round(self.get_macro(macro), 2)))


class MealScheduleDay():
    '''
    Represents 1 day in a MealSchedule
    '''
    def __init__(self, day, meals=None):
        '''
        day: Str in days global variable
        meals: either a Meal or a List of Meal
        '''
        self.day = day
        self.meals = []
        if isinstance(meals, Meal):
            self.meals.append(meals)
        elif isinstance(meals, list):
            self.meals.extend(meals)

    def add_meals(self, meals):
        '''
        meals: either Meal of List of Meal
        '''
        if isinstance(meals, Meal):
            self.meals.append(meals)
        elif isinstance(meals, list):
            self.meals.extend(meals)

    def get_macro(self, macro):
        total = 0
        for meal in self.meals:
            total += meal.get_macro(macro)
        return total

    def show_meals(self):
        print("On " + self.day + ", the following meals have been planned:")
        for meal in self.meals:
            print("- " + meal.meal_name + " (" + meal.meal_type + ")")

    def show_macros(self):
        print("The meals planned for " + self.day + " have the following Macros:")
        for macro in macros:
            print("    " + macro + ": " + str(round(self.get_macro(macro), 2)))
            

class MealSchedule():
    '''
    Represents 1 week of planned meals in a MealPlan
    '''
    def __init__(self):
        self.schedule = {}
        for day in days:
            self.schedule[day] = MealScheduleDay(day)

    def add_meals_to_day(self, day, meals):
        '''
        day: Str in days list
        meals: Meal or List of Meal
        '''
        self.schedule[day].add_meals(meals)

    def replace_day(self, day):
        '''
        day: MealScheduleDay
        '''
        self.schedule[day.day] = day

    def get_days_macro(self, day, macro):
        '''
        day: Str
        macro: Str
        '''
        self.schedule[day].get_macro(macro)

    def show_meals(self):
        for day in days:
            self.schedule[day].show_meals()

    def show_macros(self):
        for day in days:
            self.schedule[day].show_macros()


class Diet():
    '''
    Represents a type of diet
    '''
    def __init__(self, daily_cals, cal_proportions):
        '''    
        daily_cals: Int or Float
        cal_proportions: List of Int or Float:
        [percent_carbs, percent_fats, percent_proteins]
        What percentage of your daily calories will be from proteins,
        carbohydrates, and fats.
        
        Precondition: cal_proportions[0] + cal_proportions[1]
                      + cal_proportions[2] = 100
        '''
        self.caloric_needs = {"percent_carbs" : cal_proportions[0],
                              "percent_fats" : cal_proportions[1],
                              "percent_proteins" : cal_proportions[2],
                              "calories" : daily_cals, 
                              "cals_carbs" : (daily_cals * (cal_proportions[0] / 100)),
                              "cals_fats" : (daily_cals * (cal_proportions[1] / 100)),
                              "cals_proteins" : (daily_cals * (cal_proportions[2] / 100))}

    def show_caloric_needs(self):
        print("Daily Calorie Requirements of Diet:")
        print("  Total Calories: " + str(round(self.caloric_needs["calories"], 2)))
        print("  Calories from Carbohydrates: " + str(round(self.caloric_needs["cals_carbs"], 2)))
        print("  Calories from Fats: " + str(round(self.caloric_needs["cals_fats"], 2)))
        print("  Calories from Protein: " + str(round(self.caloric_needs["cals_proteins"], 2)))

    def get_cal_proportions(self):
        '''
        Returns cal_proportions: List of Int or Float:
        [percent_carbs, percent_fats, percent_proteins]
        '''
        return [self.caloric_needs["percent_carbs"],
                self.caloric_needs["percent_fats"],
                self.caloric_needs["percent_proteins"]]
                
    def change_total_calories(self, new_total):
        self.caloric_needs["calories"] = new_total
        self.caloric_needs["cals_carbs"] = daily_cals * (self.caloric_needs["percent_carbs"] / 100)
        self.caloric_needs["cals_fats"] = daily_cals * (self.caloric_needs["percent_fats"] / 100)
        self.caloric_needs["cals_proteins"] = daily_cals * (self.caloric_needs["percent_proteins"] / 100)
        
    def change_cal_proportions(self, new_needs):
        '''
        new_needs: List of Int or Float: [percent_carbs, percent_fats, percent_proteins]

        Precondition: new_needs[0] + new_needs[1] + new_needs[2] = 100
        '''
        self.caloric_needs["cals_carbs"] = self.caloric_needs["calories"] * (new_needs[0] / 100)
        self.caloric_needs["cals_fats"] = self.caloric_needs["calories"] * (new_needs[1] / 100)
        self.caloric_needs["cals_proteins"] = self.caloric_needs["calories"] * (new_needs[2] / 100)


class MealPlan():
    '''
    Represents a meal plan
    '''
    def __init__(self, diet, meal_schedule):
        '''
        diet: Diet
        meal_schedule: MealSchedule
        '''
        self.diet = diet
        self.meal_schedule = meal_schedule

    def show_plan_success(self):
        '''
        There is a 5% Margin of Error
        '''
        print("According to your current Diet:")
        for day in self.meal_schedule.schedule:
            print("On " + day + ", you should consume:")
            for macro in macros:
                prescribed = self.diet.caloric_needs[macro]
                actual = self.meal_schedule.schedule[day].get_macro(macro)
                difference = prescribed - actual
                if difference > 0.05 * prescribed: # 5% Margin of Error
                    print("  " + str(round(difference, 2)) + " more " + macro_name_converter(macro))
                elif difference < -0.05 * prescribed: # 5% Margin of Error
                    print("  " + str(round(-difference, 2)) + " less " + macro_name_converter(macro))

    def change_plan(self, diet_or_schedule):
        '''
        diet_or_schedule: Diet or MealSchedule
        '''
        if isinstance(diet_or_schedule, Diet):
            self.diet = diet_or_schedule
        elif isinstance(diet_or_schedule, MealSchedule):
            self.meal_schedule = diet_or_schedule

        

        


