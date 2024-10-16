import os
from profile import *
##from meal_planner.meal_planner import *
##from meal_planner.cookbook import meal_list
##import meal_planner.cookbook as cb
from exercise_planner.exercise_planner import *
from exercise_planner.my_exercises import *

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


#### Testing Meal Planning ####

##andy_profile = Profile((5,5), 155, 31, "Male", "Moderately Active")
##andy_diet = Diet(2100, [45, 25, 30])
##schedule = MealSchedule()
##monday = [cb.omlett_breakfast, cb.pasta, cb.chicken_dinner, cb.parfait_snack, cb.fruit_salad_snack, cb.popcorn_snack, cb.protein_drink]
##tuesday = [cb.omlett_breakfast, cb.soup_and_sandwhich, cb.chicken_dinner, cb.parfait_snack, cb.fruit_salad_snack, cb.popcorn_snack, cb.protein_drink]
##wednesday = [cb.omlett_breakfast, cb.pasta, cb.chicken_dinner, cb.parfait_snack, cb.fruit_salad_snack, cb.popcorn_snack, cb.protein_drink]
##thursday = [cb.omlett_breakfast, cb.soup_and_sandwhich, cb.chicken_dinner, cb.parfait_snack, cb.fruit_salad_snack, cb.popcorn_snack, cb.protein_drink]
##friday = [cb.omlett_breakfast, cb.pasta, cb.chicken_dinner, cb.parfait_snack, cb.fruit_salad_snack, cb.popcorn_snack, cb.protein_drink]
##saturday = [cb.omlett_breakfast, cb.soup_and_sandwhich, cb.chicken_dinner, cb.parfait_snack, cb.fruit_salad_snack, cb.popcorn_snack, cb.protein_drink]
##sunday = [cb.omlett_breakfast, cb.pasta, cb.chicken_dinner, cb.parfait_snack, cb.fruit_salad_snack, cb.popcorn_snack, cb.protein_drink]
##schedule.add_meals_to_day("Monday", monday)
##schedule.add_meals_to_day("Tuesday", tuesday)
##schedule.add_meals_to_day("Wednesday", wednesday)
##schedule.add_meals_to_day("Thursday", thursday)
##schedule.add_meals_to_day("Friday", friday)
##schedule.add_meals_to_day("Saturday", saturday)
##schedule.add_meals_to_day("Sunday", sunday)
##mealplan = MealPlan(andy_diet, schedule)
##mealplan.show_plan_success()  
##mealplan.show_plan_adequacy()


#### Testing Exercise Planner ####

##for exercise in exercise_list:
##    print(exercise.show_data())
    
pushday = WorkOut("Push Day", [bench_press, triceps_extension, shoulder_press, push_away, lat_arm_raise])
pullday = WorkOut("Pull Day", [pull_up, bicep_curl, pull_down, row, shrug])
legday = WorkOut("Leg Day", [squat, romanian_deadlift, leg_curl, leg_extension])

##print(pushday)
##print(pullday)
##print(legday)

print(pushday.muscle_groups_worked())

andysprogram = Program("Andy's Test Program", "Resistence Training", [pushday, pullday, legday])
print(andysprogram.muscle_groups_neglected())




