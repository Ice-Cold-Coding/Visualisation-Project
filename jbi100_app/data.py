import pandas as pd

def get_data(filename):
    # Read data
    df = pd.read_csv(filename, low_memory=False)

    # Any further data preprocessing can go her

    return df
