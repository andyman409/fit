from meal_planner import Meal, MealScheduleDay, MealSchedule, MealPlan, Diet
##from exercise_planner import
from profile import Profile
import cookbook as cb
from cookbook import meal_list


######################################
#            Fitness App             #
######################################

def profile_constructor():
    name = input("Enter your Name: ")
    print("Enter your Height (in ft., in.): ")
    feet = int(input("    Feet: "))
    inches = int(input("    Inches: "))
    height = (feet, inches)
    weight = int(input("Enter your Weight (in lbs.): "))
    age = int(input("Enter your Age: "))
    sex = input("Are you Male or Female? ").capitalize()
    while not ((sex == "Male") or (sex == "Female")):
        print("Invalid entry")
        sex = input("Are you Male or Female? ").capitalize()
    return Profile(height, weight, age, sex)
    lifestyle = input("Is your lifestyle Sedentary, Lightly Active, Moderately Active, Very Active, or Extremely Active? ").capitalize()
    while lifestyle not in katch_mcardle_multipliers:
        print("Invalid entry")
        sex = input("Is your lifestyle Sedentary, Lightly Active, Moderately Active, Very Active, or Extremely Active? ").capitalize()
    return Profile(height, weight, age, sex, lifestyle)


##moms_profile = Profile((5, 3), 170, 55, "Female", "Lightly Active")
andy_profile = Profile((5, 5), 155, 31, "Male", "Moderately Active")
##andy_profile.show_stats()
print(" ")
default_diet = Diet(2100, [45, 25, 30])
##default_diet.show_caloric_needs()
print(" ")
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
mealplan.show_plan_success()

##for meal in meal_list:
##    meal.show_macros()



