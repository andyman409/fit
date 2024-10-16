import os
import pandas as pd
import exercise_planner.strength_standards.ss_reader as ss_reader

######################################
#        Exercise Planner            #
######################################

######## GENERAL FUNCTIONS & GLOBAL VARIABLES ########

##exs_s =	"Exercise 	Short YouTube Demonstration	In Depth YouTube Technique	Difficulty Level	Muscle Group 	Prime Mover Muscle	Secondary Muscle	Tertiary Muscle	Primary Equipment 	# Primary Items	Secondary Equipment	# Secondary Items	Posture	Single or Double Arm	Continuous or Alternating Arms 	Grip	Load Position (Ending)	Combination Exercises	Movement Pattern #1	Movement Pattern #2	Movement Pattern #3	Plane Of Motion #1	Plane Of Motion #2	Plane Of Motion #3	Mechanics	Terms of Laterality	Exercise Classification"
##exs = exs_s.split("	")
exs_data_labels = ['Exercise ', 'Short YouTube Demonstration', 'In Depth YouTube Technique', 'Difficulty Level', 'Muscle Group ', 'Prime Mover Muscle', 'Secondary Muscle', 'Tertiary Muscle', 'Primary Equipment ', '# Primary Items', 'Secondary Equipment', '# Secondary Items', 'Posture', 'Single or Double Arm', 'Continuous or Alternating Arms ', 'Grip', 'Load Position (Ending)', 'Combination Exercises', 'Movement Pattern #1', 'Movement Pattern #2', 'Movement Pattern #3', 'Plane Of Motion #1', 'Plane Of Motion #2', 'Plane Of Motion #3', 'Mechanics', 'Terms of Laterality', 'Exercise Classification']

muscle_groups = {"Chest" : ["Pectoralis Major", "Serratus Anterior"],
                 "Triceps" : ["Triceps Brachii"],
                 "Shoulders" : ["Posterior Deltoids", "Medial Deltoids", "Anterior Deltoids", "Teres Major", 'Infraspinatus', "Teres Minor", 'Subscapularis'],
                 "Back" : ["Latissimus Dorsi", "Erector Spinae", 'Rhomboids'],
                 "Trapezius" : ["Upper Trapezius", "Lower Trapezius"],
                 "Biceps" : ["Biceps Brachii", "Brachialis"],
                 "Quadriceps" : ["Quadriceps Femoris"],
                 "Hamstrings" : ["Biceps Femoris"],
                 "Glutes" : ["Gluteus Maximus", "Gluteus Medius", "Gluteus Minimus", "Tensor Fasciae Latae"],
                 "Calves" : ["Gastrocnemius", "Soleus", 'Tibialis Anterior'],
                 "Adductors" : ["Adductor Magnus"],
                 "Abdominals" : ["Rectus Abdominis", "Obliques"],
                 "Forearms": ["Brachioradialis"]}

muscles = ['Rectus Abdominis', 'Gluteus Maximus', 'Obliques', 'Pectoralis Major', 'Adductor Magnus', 'Latissimus Dorsi', 'Posterior Deltoids', 'Biceps Brachii', 'Biceps Femoris', 'Gluteus Medius', 'Gastrocnemius', 'Quadriceps Femoris', 'Medial Deltoids', 'Anterior Deltoids', 'Subscapularis', 'Upper Trapezius', 'Serratus Anterior', 'Brachioradialis', 'Triceps Brachii', 'Erector Spinae', 'Tibialis Anterior', 'Lower Trapezius', 'Infraspinatus', 'Gluteus Minimus', 'Soleus', 'Teres Major', 'Brachialis', 'Rhomboids', 'Tensor Fasciae Latae', 'Teres Minor']

program_types = ["Aerobics", "Resistence Training", "Balance & Flexibility"]

cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
exsdf = pd.read_excel('strength+to+overcome+exercise+database+1.1.xlsx',
                      sheet_name="Exercises",
                      skiprows=11)
os.chdir(cwd)

def valid_sex(sex):
    return sex.title() == "Male" or sex.title() != "Female"

def get_sexed_label(sex):
    if valid_sex(sex):
        if sex.title() == "Male":
            return "One Rep Max - Male"
        elif sex.title() == "Female":
            return "One Rep Max - Female"
    else:
        raise Exception("Invalid Entry. Must be 'Male' or 'Female' (Not Case Sensitive)")

class Exercise():
    def __init__(self, exs_name_or_data, new_name):
        '''
        exs_name_or_data: Str or Dict of formatted data
        new_name: Str
        '''
        self.name = new_name
        self.exs_data = {}
        if isinstance(exs_name_or_data, str):
            for exercise in exsdf.index:
                if exsdf.loc[exercise, "Exercise "] == exs_name_or_data:
                    for data_label in exs_data_labels:
                        self.exs_data[data_label.strip()] = str(exsdf.loc[exercise, data_label]).strip()
        else:
            self.exc_data = exs_name_or_data
        self.exs_data["One Rep Max - Male"] = "No Data Recorded"
        self.exs_data["One Rep Max - Female"] = "No Data Recorded"

    def __str__(self):
        return self.name

    def add_orm(self, sex, ss_dataset_id):
        sexed_label = get_sexed_label(sex)
        result = {}
        ssdf = ss_reader.get_ss(ss_dataset_id)
        for body_weight in ssdf.index:
            for i in range(30):
                if ssdf.loc[body_weight, "Bodyweight"] == (i * 10) + 10:
                    result[(i * 10) + 10] = {}
                    for strength_level in ["Beginner", "Novice", "Intermediate", "Advanced", "Elite"]:
                        result[(i * 10) + 10][strength_level] = float(ssdf.loc[body_weight, strength_level])
        self.exs_data[sexed_label] = result
        
    def get_data(self, data):
        return self.exs_data[data]

    def show_data(self):
        result = ""
        for exs_data in self.exs_data:
            result += "\n" + "\t"
            if exs_data != "One Rep Max - Male" and exs_data != "One Rep Max - Female":
                 result += exs_data +  " : " + str(self.get_data(exs_data))
            elif isinstance(self.get_data(exs_data), dict):
                result += exs_data +  " : "
                for weight in self.get_data(exs_data):
                    result += "\n" + "\t" + "\t" + " for " + str(weight) +  " lbs :"
                    for standard in self.get_data(exs_data)[weight]:
                        result += "\n" + "\t" + "\t" + "\t" + standard + " : " + str(self.get_data(exs_data)[weight][standard])
        return "This Exercise Object contains the following data: {r}".format(r=result)

    def get_orm(self, sex, body_weight, strength_level):
        sexed_label = get_sexed_label(sex)
        if isinstance(self.get_data(sexed_label), str):
            raise Exception("This exercise has no One Rep Max data recorded")
        else:
            return self.get_data(sexed_label)[body_weight][strength_level]      

    def show_muscle_groups(self):
        result = ""
        if self.get_data("Secondary Muscle") != "nan":
            result += "\n" + "\t" + "It also hits the " + self.get_data("Secondary Muscle") + " as a Secondary Muscle"
        if self.get_data("Tertiary Muscle") != "nan":
            result += "\n" + "\t" + "And hits the " + self.get_data("Tertiary Muscle") + " as a Tertiary Muscle"
        return "For the Exercise " + self.name + ":" + "\n" + "\t" + "The Prime Mover Muscle is the " + self.get_data("Prime Mover Muscle") + "{r}".format(r=result)

class Set():
    def __init__(self, reps=1, weight_lbs=0, time_mins_secs=(0,0)):
        '''
        '''
        self.reps = reps
        self.weight_lbs = weight_lbs
        self.time_mins_secs = time_mins_secs
        self.weight_kgs = weight_lbs * 0.453592
        self.secs = (time_mins_secs[0] * 60) + time_mins_secs[1]

    def __str__(self):
        return "you did " + str(self.reps) + " reps at " + str(self.weight_lbs) + " lbs."

class Session():
    def __init__(self, exercise, data=[], set_type="Default"):
        '''
        exercise = an Exercise object
        data: List of Set
        '''
        self.exercise = exercise
        self.name = exercise.name
        self.num_sets = len(data)
        self.sets = data

    def estimate_orm(self):
        '''
        Uses The Brzycki Equation
        '''
        orm_each_set = []
        for e_set in self.sets:
            orm_each_set.append(e_set.weight_lbs / (1.0278 - (0.0278 * e_set.reps)))            
        return max(orm_each_set)

    def __str__(self):
        result = ""
        for i in range(self.num_sets):
            result += "\n" + "\t" + "On set #" + str(i+1) + ", " + str(self.sets[i])
        return (str(self.num_sets) + " sets of " + self.name  + "{r}".format(r=result)
                + "\n" + "\t" + "Your One Rep Max would be approximately " + str(round(self.estimate_orm(), 2)) + " lbs.")
    
class WorkOut():
    def __init__(self, day, sessions):
        self.day = day
        self.sessions = sessions

    def __str__(self):
        result = ""
        for session in self.sessions:
            result += "\n" + "\t" + str(session)
        return "On " + self.day + ", you have the following exercise sessions programmed:" + "{r}".format(r=result)

    def muscle_groups_worked(self):
        mgw = []
        for session in self.sessions:
            mgw.append(session.exercise.get_data("Muscle Group"))
        return list(set(mgw))
            
class Program():
    def __init__(self, name, program_type, workouts):
        '''
        name: Str
        program_type = Str in program_types global variable
        workouts: List of WorkOut
        '''
        self.name = name
        self.program_type = program_type
        self.workouts = workouts

    def muscle_groups_neglected(self):
        mgn = list(muscle_groups.keys())
        mgw = []
        for workout in self.workouts:
            print(list(set(mgw)))
            mgw.extend(workout.muscle_groups_worked())
        print(list(set(mgw)))
        for mg in mgw:
            if mg in mgn:
                mgn.remove(mg)
        return list(set(mgn))

class Routine():
     def __init__(self, name, programs):
        '''
        name: Str
        programs: List of Program
        '''
        self.name = name
        self.programs = programs
    
