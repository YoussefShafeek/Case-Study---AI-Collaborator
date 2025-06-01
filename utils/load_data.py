# Name: Youssef Shafeek
# Date: 05/26/2025
# File Description: This utility module is responsible for loading the customer feedback dataset 
# from a CSV file into a pandas DataFrame. This allows the system to access and manipulate 
# structured feedback data for downstream analysis.

import pandas as pd

# This function takes in a CSV file and returns it as a pandas DataFrame
def load_feedback_data(filepath: str = "data/CNew_Feedback_Dataset_1000.csv") -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df
