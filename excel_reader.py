import pandas as pd

def read_excel(file_path):

    data = pd.read_excel(file_path)

    return data