from exercise_planner.exercise_planner import *

######################################
#              Exercises             #
######################################

############# PUSH #############

bench_press = Exercise("Barbell Bench Press", "Bench Press (Barbell)")
triceps_extension = Exercise("EZ Bar Lying Tricep Extension ", "Tricep Extension (Bench, Barbell)")
shoulder_press = Exercise("Barbell Overhead Press", "Shoulder Press (Overhead, Barbell, Standing)")
push_away = Exercise("Cable Rope Standing Overhead Tricep Extension", "Push Away (Triceps, Rope)")
lat_arm_raise = Exercise("Dumbbell Lateral Raise", "Raise (Lateral)")

############# PULL #############

pull_up = Exercise("Superband Assisted Wide Grip Pull Up", "Pull Up")
bicep_curl = Exercise("Dumbbell Alternating Bicep Curl", "Bicep Curl (Alternating, Dumbbell)")
pull_down = Exercise("Cable Wide Grip Lat Pulldown", "Pull Down (Seated)")
row = Exercise("Cable Seated V Grip Low Row", "Row (Seated, Low)")
shrug = Exercise("Barbell Shrug", "Shrugs (Barbell)")

############# LEGS #############

squat = Exercise("Barbell Low Bar Cyclist Squat", "Squat (Weighted, Back, Barbell, Elevated)")
romanian_deadlift = Exercise("Barbell Romanian Deadlift", "Deadlift (Romanian, Barbell)")
lc ={'Exercise ' : "Leg Curl",
     'Short YouTube Demonstration' : "",
     'In Depth YouTube Technique' : "",
     'Difficulty Level' : "Beginner",
     'Muscle Group' : "Hamstrings",
     'Prime Mover Muscle' : "Biceps Femoris",
     'Secondary Muscle' : "",
     'Tertiary Muscle' : "",
     'Primary Equipment' : "Machine",
     '# Primary Items' : "1",
     'Secondary Equipment' : "",
     '# Secondary Items' : "",
     'Posture' : "Seated",
     'Single or Double Arm' : "No Arms",
     'Continuous or Alternating Arms' : "Continuous",
     'Grip' : "No Grip",
     'Load Position (Ending)' : "Overhead",
     'Combination Exercises' : "Single Exercise",
     'Movement Pattern #1' : "Horizontal Pull",
     'Movement Pattern #2' : "",
     'Movement Pattern #3' : "",
     'Plane Of Motion #1' : "Sagittal",
     'Plane Of Motion #2' : "",
     'Plane Of Motion #3' : "",
     'Mechanics' : "Isolation",
     'Terms of Laterality' : "Bilateral",
     'Exercise Classification' : "Bodybuilding"}
le ={'Exercise' : "Leg Extension",
     'Short YouTube Demonstration' : "",
     'In Depth YouTube Technique' : "",
     'Difficulty Level' : "Beginner",
     'Muscle Group' : "Quadriceps",
     'Prime Mover Muscle' : "Quadriceps Femoris",
     'Secondary Muscle' : "",
     'Tertiary Muscle' : "",
     'Primary Equipment' : "Machine",
     '# Primary Items' : "1",
     'Secondary Equipment' : "",
     '# Secondary Items' : "",
     'Posture' : "Seated",
     'Single or Double Arm' : "No Arms",
     'Continuous or Alternating Arms' : "Continuous",
     'Grip' : "No Grip",
     'Load Position (Ending)' : "Overhead",
     'Combination Exercises' : "Single Exercise",
     'Movement Pattern #1' : "Horizontal Push",
     'Movement Pattern #2' : "",
     'Movement Pattern #3' : "",
     'Plane Of Motion #1' : "Sagittal",
     'Plane Of Motion #2' : "",
     'Plane Of Motion #3' : "",
     'Mechanics' : "Isolation",
     'Terms of Laterality' : "Bilateral",
     'Exercise Classification' : "Bodybuilding"}
leg_curl = Exercise(lc, "Leg Curl (Seated)")
leg_extension = Exercise(le, "Leg Extension (Seated)")

######################################
#                 ORMS               #
######################################

############# PUSH #############

bench_press.add_orm("Male", "bench_press.xlsx")
triceps_extension.add_orm("Male", "lying_triceps_extension.xlsx")
shoulder_press.add_orm("Male", "shoulder_press.xlsx")
push_away.add_orm("Male", "cable_overhead_triceps_extensions.xlsx")

############# PULL #############

pull_up.add_orm("Male", "pull_up.xlsx")
bicep_curl.add_orm("Male", "bicep_curl.xlsx")
pull_down.add_orm("Male", "pull_down.xlsx")
shrug.add_orm("Male", "shrug.xlsx")

############# LEGS #############

squat.add_orm("Male", "squat.xlsx")
romanian_deadlift.add_orm("Male", "romanian_deadlift.xlsx")
leg_curl.add_orm("Male", "leg_curl_seated.xlsx")
leg_extension.add_orm("Male", "leg_extension_seated.xlsx")


############# GLOBAL VARIABLE #############

exercise_list = [bench_press, triceps_extension, shoulder_press, push_away, lat_arm_raise,
                 pull_up, bicep_curl, pull_down, row, shrug,
                 squat, romanian_deadlift, leg_curl, leg_extension]


######################################
#              MY PRS                #
######################################


############# PUSH #############

bpd = [Set(10, 120), Set(10, 120), Set(7, 120), Set(7, 120)]
ted = [Set(20, 20), Set(13, 30), Set(12, 30), Set(14, 20)]
spd = [Set(12, 17.5), Set(6, 17.5), Set(7, 15), Set(5, 15)]
pad = [Set(18, 40), Set(9, 37.5), Set(10, 35), Set(8, 32.5)]
lard = [Set(10, 10), Set(10, 10), Set(10, 10), Set(10, 10)]

bench_press = Session(bench_press, bpd)
triceps_extension = Session(triceps_extension, ted)
shoulder_press = Session(shoulder_press, spd)
push_away = Session(push_away, pad)
lat_arm_raise = Session(lat_arm_raise, lard)

############# PULL #############

pud = [Set(3, 0), Set(1, 0), Set(1, 0)]
bcd = [Set(10, 25), Set(10, 25), Set(10, 25), Set(8, 25)]
pdd = [Set(20, 70), Set(17, 70), Set(24, 55), Set(22, 55)]
rd = [Set(20, 40), Set(20, 55), Set(20, 55), Set(20, 55)]
sd = [Set(7, 25), Set(7, 25), Set(6, 25)]

pull_up = Session(pull_up, pud)
bicep_curl = Session(bicep_curl, bcd)
pull_down = Session(pull_down, pdd)
row = Session(row, rd)
shrug = Session(shrug, sd)

############# LEGS #############

sd = [Set(10, 80), Set(10, 85), Set(10, 90), Set(10, 90)]
rdd = [Set(9, 90), Set(8, 90), Set(8, 90), Set(7, 90)]
lcd = [Set(14, 35), Set(16, 32.5), Set(14, 30), Set(14, 30)]
led = [Set(13, 30), Set(13, 27.5), Set(11, 25), Set(10, 25)]

squat = Session(squat, sd)
romanian_deadlift = Session(romanian_deadlift, rdd)
leg_curl = Session(leg_curl, lcd)
leg_extension = Session(leg_extension, led)


############# GLOBAL VARIABLE #############

session_list =  [bench_press, triceps_extension, shoulder_press, push_away, lat_arm_raise,
                 pull_up, bicep_curl, pull_down, row, shrug,
                 squat, romanian_deadlift, leg_curl, leg_extension]
