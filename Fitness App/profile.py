######################################
#              Profile               #
######################################

######## GENERAL FUNCTIONS & GLOBAL VARIABLES ########

katch_mcardle_multipliers = {"Sedentary" : 1.2,
                             "Lightly Active" : 1.375,
                             "Moderately Active" : 1.55,
                             "Very Active" : 1.725,
                             "Extremely Active" : 1.9}

class Profile():
    def __init__(self, height_ft_in, weight_lbs, age, sex, lifestyle):
        '''
        height_ft_in: Tuple of Int (Feet, Inches)
        weight_lbs: Int
        age: Int
        sex: Str: either Male or Female
        '''
        self.height_ft_in = height_ft_in
        self.height_cm = (height_ft_in[0] * 30.48) + (height_ft_in[1] * 2.54)
        self.height_in = self.height_cm * 0.393701
        self.weight_lbs = weight_lbs
        self.weight_kgs = self.weight_lbs * 0.453592
        self.age = age
        self.sex = sex
        self.lifestyle = lifestyle
        self.bmi = self.weight_kgs / (self.height_cm * 0.01)**2
##        self.grams_protein_for_maintenance = 0.8 * self.weight_lbs
##        self.cals_protein_for_maintenance = self.grams_protein_for_maintenance * 4

    def get_bodyfat_percentage(self):        
        if self.sex == "Male":
            bf_modifier = 16.2
        elif self.sex == "Female":
            bf_modifier = 5.4
        return ((1.20 * self.bmi) + (0.23 * self.age)) - bf_modifier

    def update_weight(self, new_weight_lbs):
        self.weight_lbs = new_weight_lbs
        self.weight_kgs = self.weight_lbs * 0.453592
        self.bmi = self.weight_kgs / (self.height_cm * 0.01)**2

    def update_lifestyle(self, new_lifestyle):
        if new_lifestyle in katch_mcardle_multipliers:
            self.lifestyle = new_lifestyle

    def show_bmi(self):
        print("Your BMI is: " + str(round(self.bmi, 2)))
        if self.bmi < 18.5:
            print("This is considered underweight")
        elif 18.5 < self.bmi < 24.9:
            print("This is considered a healthy weight")
        elif 24.9 < self.bmi < 29.9:
            print("This is considered overweight")
        elif 30 < self.bmi:
            print("This is considered obese")

    def get_bmr(self):
        '''
        bmr = Basal Metabolic Rate

        Uses the Harris-Benedict Formula for BMR
        '''
        if self.sex == "Male":
            return 66.47 + (6.24 * self.weight_lbs) + (12.7 * self.height_in) - (6.8 * self.age)
        elif self.sex == "Female":
            return 655.1 + (4.35 * self.weight_lbs) + (4.7 * self.height_in) - (4.7 * self.age)

    def get_tdee(self):
        '''
        tdee = Total Daily Energy Expenditure. Equivalent to Maintenance Calories.
        lifestyle = Str in [Sedentary, Lightly Active, Moderately Active, Very Active,
                    Extremely Active]
        '''
        return katch_mcardle_multipliers[self.lifestyle] * self.get_bmr()

    def show_recommendations_for_cutting(self, lbs_per_week=1):
        '''
        lbs_per_week = Int in [1, 2]. Default is 1
        '''
        dc = self.get_tdee() - ((lbs_per_week * 3500) / 7)
        protein_cals = 0.9 * self.weight_lbs * 4
        fat_cals = 0.3 * dc
        print("If you are on a Cut, and your goal is to lose " + str(lbs_per_week) + " lbs. of body fat per week, then:")
        print("    Your daily caloric intake should be: " + str(round(dc, 2)))
        print("    You should consume at least " + str(round(protein_cals, 2)) + " Calories from Proteins")
        print("    You should consume at most " + str(round(fat_cals, 2)) + " Calories from Fats")

    def show_recommendations_for_bulking(self, lbs_per_week=1):
        '''
        lbs_per_week = Int in [1, 2]. Default is 1
        '''
        dc = self.get_tdee() + ((lbs_per_week * 2250) / 7)
        surplus = (lbs_per_week * 2250) / 7
        protein_cals = 0.8 * self.weight_lbs * 4
        print("If you are on a Bulk, and your goal is to gain " + str(lbs_per_week) + " lbs. of lean muscle mass per week, then:")
        print("    Your daily caloric intake should be: " + str(round(dc, 2)))
        print("    The surplus " + str(round(surplus, 2)) + " calories should be primarily from Carbohydrates")
        print("    You should consume at least " + str(round(protein_cals, 2)) + " Calories from Proteins")

    def show_stats(self):
        print("Your Age is: " + str(self.age))
        print("Your Height is: " + str(self.height_ft_in[0]) + " ft., " + str(self.height_ft_in[1]) + " in.")
        print("Your Weight is: " + str(self.weight_lbs) + " lbs.")
        self.show_bmi()
        print("Your Body Fat Percentage is: " + str(round(self.get_bodyfat_percentage(), 2)) + "%")
        print("Your lifestyle is: " + self.lifestyle)
        print("Your Basal Metabolic Rate is: " + str(round(self.get_bmr(), 2)))
        print("Your Total Daily Energy Expenditure is: " + str(round(self.get_tdee(), 2)))
        self.show_recommendations_for_cutting()
        self.show_recommendations_for_bulking()




        
