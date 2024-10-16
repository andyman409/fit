import os
import pandas as pd

def get_ss(ss_dataset_id):
    cwd = os.getcwd()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    result = pd.read_excel(ss_dataset_id)
    os.chdir(cwd)
    return result
