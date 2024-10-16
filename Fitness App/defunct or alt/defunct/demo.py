import pandas as pd


##df = pd.DataFrame({'col1': [1, 2],
##                   'col2': [0.5, 0.75]},
##                  index=['row1', 'row2'])
##print(df)
##print(df['col1']['row1'])



df = pd.read_excel(r"C:\Users\andys\Desktop\Meal Planning\meal_planner_data.xlsx",
                   sheet_name="Diets",
                   index_col="Diet",
                   converters={"Protein" : int,
                               "Carbs" : int,
                               "Fat" : int}
                   )

print(isinstance(df, pd.DataFrame))
print(df)
print(df["Protein"])
print(df["Protein"]["Low Fat"])



##df = pd.read_excel(r"C:\Users\andys\Desktop\Meal Planning\meal_planner_data.xlsx", "Ingredients")
##print(isinstance(df, pd.DataFrame))
##print(df)
##del df[0]
##print(df)
##print(df["calories"]["1 oz Raw Ground Beef"])





##omlett_ingredients = [
##ingredients["1 Chicken Egg"] * 2,
##ingredients["1 Red Bell Pepper"] * 1/4,
##ingredients["1 White Button Mushroom"] * 2,
##ingredients["1 Medium Onion"] * 1/4,
##ingredients["1 Cup Kale"] * 1/4
##]
##
##cals = sum(omlett_ingredients['calories'])
##cals_proteins = sum(omlett_ingredients['cals_proteins'])
##cals_carbs = sum(omlett_ingredients['cals_carbs'])
##cals_fats = sum(omlett_ingredients['cals_fats'])
##
##omlett = []
##
##omplett.add(cals)
##omplett.add(cals_proteins)
##omplett.add(cals_carbs)
##omplett.add(cals_fats)
##
##print(omlett[0])
##print(omlett[1])
##print(omlett[2])
##print(omlett[3])


