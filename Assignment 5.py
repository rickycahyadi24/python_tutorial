import pandas as pd

# 1. Input
raw_data = pd.read_csv("Menu.csv")
print(raw_data)
print(raw_data.info())

# 2. Process
raw_data.sort_values(["Menu"],axis=0,inplace=True)

# 3. Output
print(raw_data)