from meal_planner import FridgeItem, Ingredient, Recipe, Meal

######################################
#             My Fridge              #
######################################

class MyFridge():
    def __init__(self):
        self.food_items = {}
        self.meals = {}

    def add_food_item(self, label, modifier):
        return FridgeItem(label, modifier)


##moms_profile = Profile((5, 3), 170, 55, "Female", "Lightly Active")
##andy_profile.show_stats()
##print(" ")
##default_diet = Diet(2100, [45, 25, 30])
##default_diet.show_caloric_needs()
##print(" ")
schedule = MealSchedule()
schedule.add_meals_to_day("Monday", [cb.omlett_breakfast, cb.pasta, cb.chicken_dinner, cb.fruit_salad_snack, cb.popcorn_snack, cb.energy_bar])
schedule.add_meals_to_day("Tuesday", [cb.omlett_breakfast, cb.lazy_chili_dogs, cb.lazy_chili_dogs, cb.chicken_dinner, cb.fruit_salad_snack, cb.energy_bar])
schedule.add_meals_to_day("Wednesday", [cb.oatmeal_meal, cb.pasta, cb.burger_dinner, cb.popcorn_snack, cb.energy_bar])
schedule.add_meals_to_day("Thursday", [cb.pancake_breakfast, cb.pasta, cb.burger_dinner, cb.parfait_snack, cb.popcorn_snack, cb.protein_drink])
schedule.add_meals_to_day("Friday", [cb.omlett_breakfast, cb.lazy_chili_dogs, cb.chicken_dinner, cb.fruit_salad_snack, cb.popcorn_snack, cb.protein_drink])
schedule.add_meals_to_day("Saturday", [cb.omlett_breakfast, cb.pasta, cb.chicken_dinner, cb.fruit_salad_snack, cb.popcorn_snack, cb.energy_bar])
schedule.add_meals_to_day("Sunday", [cb.pancake_breakfast, cb.soup_and_sandwhich, cb.chicken_dinner, cb.parfait_snack, cb.popcorn_snack, cb.energy_bar])
print(" ")
mealplan = MealPlan(default_diet, schedule)
mealplan.show_plan_adequacy()

##for meal in meal_list:
##    meal.show_macros()
##    meal.show_recipes()
##    for recipe in meal.recipes:
##        recipe.show_macros()
