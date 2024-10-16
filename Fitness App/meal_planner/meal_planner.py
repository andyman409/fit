import pandas as pd
import os

######################################
#          Meal Planner              #
######################################


######## GENERAL FUNCTIONS & GLOBAL VARIABLES ########

##nutes_s = "ID	name	Food Group	Calories	Fat (g)	Protein (g)	Carbohydrate (g)	Sugars (g)	Fiber (g)	Cholesterol (mg)	Saturated Fats (g)	Calcium (mg)	Iron, Fe (mg)	Potassium, K (mg)	Magnesium (mg)	Vitamin A, IU (IU)	Vitamin A, RAE (mcg)	Vitamin C (mg)	Vitamin B-12 (mcg)	Vitamin D (mcg)	Vitamin E (Alpha-Tocopherol) (mg)	Added Sugar (g)	Net-Carbs (g)	Water (g)	Omega 3s (mg)	Omega 6s (mg)	PRAL score	Trans Fatty Acids (g)	Soluble Fiber (g)	Insoluble Fiber (g)	Sucrose (g)	Glucose (Dextrose) (g)	Fructose (g)	Lactose (g)	Maltose (g)	Galactose (g)	Starch (g)	Total sugar alcohols (g)	Phosphorus, P (mg)	Sodium (mg)	Zinc, Zn (mg)	Copper, Cu (mg)	Manganese (mg)	Selenium, Se (mcg)	Fluoride, F (mcg)	Molybdenum (mcg)	Chlorine (mg)	Thiamin (B1) (mg)	Riboflavin (B2) (mg)	Niacin (B3) (mg)	Pantothenic acid (B5) (mg)	Vitamin B6 (mg)	Biotin (B7) (mcg)	Folate (B9) (mcg)	Folic acid (mcg)	Food Folate (mcg)	Folate DFE (mcg)	Choline (mg)	Betaine (mg)	Retinol (mcg)	Carotene, beta (mcg)	Carotene, alpha (mcg)	Lycopene (mcg)	Lutein + Zeaxanthin (mcg)	Vitamin D2 (ergocalciferol) (mcg)	Vitamin D3 (cholecalciferol) (mcg)	Vitamin D (IU) (IU)	Vitamin K (mcg)	Dihydrophylloquinone (mcg)	Menaquinone-4 (mcg)	Fatty acids, total monounsaturated (mg)	Fatty acids, total polyunsaturated (mg)	18:3 n-3 c,c,c (ALA) (mg)	20:5 n-3 (EPA) (mg)	22:5 n-3 (DPA) (mg)	22:6 n-3 (DHA) (mg)	Tryptophan (mg)	Threonine (mg)	Isoleucine (mg)	Leucine (mg)	Lysine (mg)	Methionine (mg)	Cystine (mg)	Phenylalanine (mg)	Tyrosine (mg)	Valine (mg)	Arginine (mg)	Histidine (mg)	Alanine (mg)	Aspartic acid (mg)	Glutamic acid (mg)	Glycine (mg)	Proline (mg)	Serine (mg)	Hydroxyproline (mg)	Alcohol (g)	Caffeine (mg)	Theobromine (mg)	Serving Weight 1 (g)	Serving Description 1 (g)	Serving Weight 2 (g)	Serving Description 2 (g)	Serving Weight 3 (g)	Serving Description 3 (g)	Serving Weight 4 (g)	Serving Description 4 (g)	Serving Weight 5 (g)	Serving Description 5 (g)	Serving Weight 6 (g)	Serving Description 6 (g)	Serving Weight 7 (g)	Serving Description 7 (g)	Serving Weight 8 (g)	Serving Description 8 (g)	Serving Weight 9 (g)	Serving Description 9 (g)	200 Calorie Weight (g)"
##nutes = nutes_s.split("	")
nutes = ['Calories', 'Fat (g)', 'Protein (g)', 'Carbohydrate (g)', 'Sugars (g)', 'Fiber (g)', 'Cholesterol (mg)', 'Saturated Fats (g)', 'Calcium (mg)', 'Iron, Fe (mg)', 'Potassium, K (mg)', 'Magnesium (mg)', 'Vitamin A, IU (IU)', 'Vitamin A, RAE (mcg)', 'Vitamin C (mg)', 'Vitamin B-12 (mcg)', 'Vitamin D (mcg)', 'Vitamin E (Alpha-Tocopherol) (mg)', 'Added Sugar (g)', 'Net-Carbs (g)', 'Water (g)', 'Omega 3s (mg)', 'Omega 6s (mg)', 'PRAL score', 'Trans Fatty Acids (g)', 'Soluble Fiber (g)', 'Insoluble Fiber (g)', 'Sucrose (g)', 'Glucose (Dextrose) (g)', 'Fructose (g)', 'Lactose (g)', 'Maltose (g)', 'Galactose (g)', 'Starch (g)', 'Total sugar alcohols (g)', 'Phosphorus, P (mg)', 'Sodium (mg)', 'Zinc, Zn (mg)', 'Copper, Cu (mg)', 'Manganese (mg)', 'Selenium, Se (mcg)', 'Fluoride, F (mcg)', 'Molybdenum (mcg)', 'Chlorine (mg)', 'Thiamin (B1) (mg)', 'Riboflavin (B2) (mg)', 'Niacin (B3) (mg)', 'Pantothenic acid (B5) (mg)', 'Vitamin B6 (mg)', 'Biotin (B7) (mcg)', 'Folate (B9) (mcg)', 'Folic acid (mcg)', 'Food Folate (mcg)', 'Folate DFE (mcg)', 'Choline (mg)', 'Betaine (mg)', 'Retinol (mcg)', 'Carotene, beta (mcg)', 'Carotene, alpha (mcg)', 'Lycopene (mcg)', 'Lutein + Zeaxanthin (mcg)', 'Vitamin D2 (ergocalciferol) (mcg)', 'Vitamin D3 (cholecalciferol) (mcg)', 'Vitamin D (IU) (IU)', 'Vitamin K (mcg)', 'Dihydrophylloquinone (mcg)', 'Menaquinone-4 (mcg)', 'Fatty acids, total monounsaturated (mg)', 'Fatty acids, total polyunsaturated (mg)', '18:3 n-3 c,c,c (ALA) (mg)', '20:5 n-3 (EPA) (mg)', '22:5 n-3 (DPA) (mg)', '22:6 n-3 (DHA) (mg)', 'Tryptophan (mg)', 'Threonine (mg)', 'Isoleucine (mg)', 'Leucine (mg)', 'Lysine (mg)', 'Methionine (mg)', 'Cystine (mg)', 'Phenylalanine (mg)', 'Tyrosine (mg)', 'Valine (mg)', 'Arginine (mg)', 'Histidine (mg)', 'Alanine (mg)', 'Aspartic acid (mg)', 'Glutamic acid (mg)', 'Glycine (mg)', 'Proline (mg)', 'Serine (mg)', 'Hydroxyproline (mg)', 'Alcohol (g)', 'Caffeine (mg)', 'Theobromine (mg)']

macros = ["Calories", "Calories from Carbohydrates", "Calories from Fats", "Calories from Protein"]

meal_types = ["Breakfast", "Lunch", "Dinner", "Snack", "Supplement"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
ingdf = pd.read_excel('MyFoodData-Nutrition-Facts-SpreadSheet-Release-1-4.xlsx',
                      sheet_name="SR Legacy and FNDDS",
                      skiprows=3)
os.chdir(cwd)

fda_rdis_food_comps = {'Carbohydrate (g)' : 275,
                       'Fat (g)' : 78,
                       'Protein (g)' : 50,
                       'Fiber (g)' : 28,
                       'Saturated Fats (g)' : 20,
                       'Cholesterol (mg)' : 300,
                       'Sodium (mg)' : 2300,
                       'Added Sugar (g)' : 50}

fda_rdis_vitamins = {'Vitamin A, RAE (mcg)' : 900,
                     'Vitamin C (mg)' : 90,
                     'Vitamin D (mcg)' : 20,
                     'Vitamin E (Alpha-Tocopherol) (mg)' : 15,
                     'Vitamin K (mcg)' : 120,
                     'Thiamin (B1) (mg)' : 1.2,
                     'Riboflavin (B2) (mg)' : 1.3,
                     'Niacin (B3) (mg)' : 16,
                     'Pantothenic acid (B5) (mg)' : 5,
                     'Vitamin B6 (mg)' : 1.7,
                     'Biotin (B7) (mcg)' : 30,
                     'Folate (B9) (mcg)' : 400,
                     'Vitamin B-12 (mcg)' : 2.4,
                     'Choline (mg)' : 550}

#Minerals are Missing Iodine, Chromium, and Chloride
fda_rdis_minerals = {'Calcium (mg)' : 1300,
                     'Copper, Cu (mg)' : 0.9,
                     'Iron, Fe (mg)' : 18,
                     'Magnesium (mg)' : 420,
                     'Manganese (mg)' : 2.3,
                     'Molybdenum (mcg)' : 45,
                     'Phosphorus, P (mg)' : 1250,
                     'Selenium, Se (mcg)' : 55,
                     'Zinc, Zn (mg)' : 11,
                     'Potassium, K (mg)' : 4700,
                     'Sodium (mg)' : 2300}

def get_name_and_unit(s):
    if s[-3:] == "(g)":
        return (s[:-3], "grams")
    elif s[-4:] == "(mg)":
        return (s[:-4], "milligrams")
    elif s[-5:] == "(mcg)":
        return (s[:-5], "micrograms")
    

######## CLASSES ########

class FridgeItem():
    def __init__(self, name, modifier=1):
        '''
        name: Str
        modifier: Float. Default is 1.
        '''
        self.name = name
        self.modifier = modifier
        self.nutes = {}
        for ing in ingdf.index:
            if ingdf.loc[ing, "name"] == self.name:
                for nute in nutes:
                    self.nutes[nute] = (float(ingdf.loc[ing, nute]) * self.modifier)
        self.nutes["Calories from Carbohydrates"] = self.nutes['Carbohydrate (g)'] * 4
        self.nutes["Calories from Fats"] = self.nutes['Fat (g)'] * 9
        self.nutes["Calories from Protein"] = self.nutes['Protein (g)'] * 4
        
    def get_nute(self, nute):
        '''
        nute: Str in nutes global variable
        '''
        return self.nutes[nute]

    def show_nutes(self):
        print(self.name + " x " + str(self.quantity) + " has the following Nutrients:")
        for nute in nutes:
            print("    " + nute + ": " + str(round(self.get_nute(nute), 2)))

class Ingredient():
    def __init__(self, fridge_item, quantity=1):
        '''
        fridge_item: FridgeItem
        quantity: Float. Default is 1.
        '''
        self.name = fridge_item.name
        self.fridge_item = fridge_item
        self.quantity = quantity
        self.nutes = fridge_item.nutes.copy()
        for nute in nutes:
            self.nutes[nute] = self.nutes[nute] * quantity
        self.nutes["Calories from Carbohydrates"] *= quantity
        self.nutes["Calories from Fats"] *= quantity
        self.nutes["Calories from Protein"] *= quantity
        
    def get_nute(self, nute):
        '''
        nute: Str in nutes global variable
        '''
        return self.nutes[nute]

    def show_nutes(self):
        print(self.name + " x " + str(self.quantity) + " has the following Nutrients:")
        for nute in nutes:
            print("    " + nute + ": " + str(round(self.get_nute(nute), 2)))        

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
    
    def get_nute(self, nute, servings=1):
        '''
        nute: Str in global variables nutes
        servings: Int (Optional). Default is 1

        Returns the quantity of the nute contained in a number of servings. Default is 1 serving.
        '''
        total = 0
        for ingredient in self.ingredients:
            total += ((ingredient.get_nute(nute) / self.servings) * servings) # double check math
        return total

    def show_nutes(self):
        print("1 " + self.name + " has the following Nutritional Information:")
        for nute in nutes:       
            print("    " + nute + ": " + str(round(self.get_nute(nute), 2)))

    def show_macros(self):
        print("1 " + self.name + " has the following Macronutrients:")
        for macro in macros:       
            print("    " + macro + ": " + str(round(self.get_nute(macro), 2)))

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

    def get_nute(self, nute):
        total = 0
        for recipe in self.recipes:
            total += recipe.get_nute(nute)
        return total

    def show_recipes(self):
        print(self.meal_name + " includes the following Recipes:")
        for recipe in self.recipes:
            print("- " + recipe.name)

    def show_nutes(self):
        print(self.meal_name + " has the following Nutritional Information:")
        for nute in nutes:
            print("    " + nute + ": " + str(round(self.get_nute(nute), 2)))

    def show_macros(self):
        print(self.meal_name + " has the following Macronutrients:")
        for macro in macros:
            print("    " + macro + ": " + str(round(self.get_nute(macro), 2)))


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

    def get_nute(self, nute):
        total = 0
        for meal in self.meals:
            total += meal.get_nute(nute)
        return total

    def show_meals(self):
        print("On " + self.day + ", the following meals have been planned:")
        for meal in self.meals:
            print("- " + meal.meal_name + " (" + meal.meal_type + ")")

    def show_nutes(self):
        print("The meals planned for " + self.day + " have the following Nutritional Information:")
        for nute in nutes:
            print("    " + nute + ": " + str(round(self.get_nute(nute), 2)))

    def show_macros(self):
        print("The meals planned for " + self.day + " have the following Macronutrients:")
        for macro in macros:
            print("    " + macro + ": " + str(round(self.get_nute(macro), 2)))
            

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

    def get_days_nute(self, day, nute):
        '''
        day: Str
        macro: Str
        '''
        self.schedule[day].get_nute(nute)

    def show_meals(self):
        for day in days:
            self.schedule[day].show_meals()

    def show_nutes(self):
        for day in days:
            self.schedule[day].show_nutes()

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
        self.caloric_needs = {"Percentage of Calories from Carbohydrates" : cal_proportions[0],
                              "Percentage of Calories from Fats" : cal_proportions[1],
                              "Percentage of Calories from Protein" : cal_proportions[2],
                              "Calories" : daily_cals, 
                              "Calories from Carbohydrates" : (daily_cals * (cal_proportions[0] / 100)),
                              "Calories from Fats" : (daily_cals * (cal_proportions[1] / 100)),
                              "Calories from Protein" : (daily_cals * (cal_proportions[2] / 100))}

    def show_caloric_needs(self):
        print("Daily Calorie Requirements of Diet:")
        print("  Total Calories: " + str(round(self.caloric_needs["Calories"], 2)))
        print("  Calories from Carbohydrates: " + str(round(self.caloric_needs["Calories from Carbohydrates"], 2)))
        print("  Calories from Fats: " + str(round(self.caloric_needs["Calories from Fats"], 2)))
        print("  Calories from Protein: " + str(round(self.caloric_needs["Calories from Protein"], 2)))

    def get_cal_proportions(self):
        '''
        Returns cal_proportions: List of Int or Float:
        '''
        return [self.caloric_needs["Percentage of Calories from Carbohydrates"],
                self.caloric_needs["Percentage of Calories from Fats"],
                self.caloric_needs["Percentage of Calories from Protein"]]
                
    def change_total_calories(self, new_total):
        self.caloric_needs["Calories"] = new_total
        self.caloric_needs["Calories from Carbohydrates"] = new_total * (self.caloric_needs["Percentage of Calories from Carbohydrates"] / 100)
        self.caloric_needs["Calories from Fats"] = new_total * (self.caloric_needs["Percentage of Calories from Fats"] / 100)
        self.caloric_needs["Calories from Protein"] = new_total * (self.caloric_needs["Percentage of Calories from Protein"] / 100)
        
    def change_cal_proportions(self, new_needs):
        '''
        new_needs: List of Int or Float:

        Precondition: new_needs[0] + new_needs[1] + new_needs[2] = 100
        '''
        self.caloric_needs["Calories from Carbohydrates"] = self.caloric_needs["Calories"] * (new_needs[0] / 100)
        self.caloric_needs["Calories from Fats"] = self.caloric_needs["Calories"] * (new_needs[1] / 100)
        self.caloric_needs["Calories from Protein"] = self.caloric_needs["Calories"] * (new_needs[2] / 100)


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
                actual = self.meal_schedule.schedule[day].get_nute(macro)
                difference = prescribed - actual
                if difference > 0.05 * prescribed: # 5% Margin of Error
                    print("  " + str(round(difference, 2)) + " more " + macro)
                elif difference < -0.05 * prescribed: # 5% Margin of Error
                    print("  " + str(round(-difference, 2)) + " less " + macro)

    def show_plan_adequacy(self):
        '''
        There is a 5% Margin of Error
        '''
        for day in self.meal_schedule.schedule:
            print("On " + day + ":")
            print(" According to the FDA Recommended Dietary Allowances for Food Components, you should consume:")
            for nute in fda_rdis_food_comps:
                prescribed = fda_rdis_food_comps[nute]
                actual = self.meal_schedule.schedule[day].get_nute(nute)
                difference = prescribed - actual
                if nute in ['Carbohydrate (g)', 'Fat (g)', 'Protein (g)', 'Fiber (g)']:
                    if difference > 0.05 * prescribed: # 5% Margin of Error
                        print("  " + str(round(difference, 2)) + " more " + get_name_and_unit(nute)[1] + " of " + get_name_and_unit(nute)[0])
                elif nute in ['Saturated Fats (g)', 'Cholesterol (mg)', 'Sodium (mg)', 'Added Sugar (g)']:
                    if difference < -0.05 * prescribed: # 5% Margin of Error
                        print("  " + str(round(-difference, 2)) + " less " + get_name_and_unit(nute)[1] + " of " + get_name_and_unit(nute)[0])
            print(" According to the FDA Recommended Dietary Allowances for Vitamins, you should consume:")
            for nute in fda_rdis_vitamins:
                prescribed = fda_rdis_vitamins[nute]
                actual = self.meal_schedule.schedule[day].get_nute(nute)
                difference = prescribed - actual
                if difference > 0.05 * prescribed: # 5% Margin of Error
                    print("  " + str(round(difference, 2)) + " more " + get_name_and_unit(nute)[1] + " of " + get_name_and_unit(nute)[0])
            print(" According to the FDA Recommended Dietary Allowances for Minerals, you should consume:")
            for nute in fda_rdis_minerals:
                prescribed = fda_rdis_minerals[nute]
                actual = self.meal_schedule.schedule[day].get_nute(nute)
                difference = prescribed - actual
                if difference > 0.05 * prescribed: # 5% Margin of Error
                    print("  " + str(round(difference, 2)) + " more " + get_name_and_unit(nute)[1] + " of " + get_name_and_unit(nute)[0])

    def change_plan(self, diet_or_schedule):
        '''
        diet_or_schedule: Diet or MealSchedule
        '''
        if isinstance(diet_or_schedule, Diet):
            self.diet = diet_or_schedule
        elif isinstance(diet_or_schedule, MealSchedule):
            self.meal_schedule = diet_or_schedule

