import pandas as pd

# 1.Input
raw_data=pd.read_csv("Menu.csv")

# 2.Process
numberOfItems=len(raw_data)
sorted_data=raw_data.sort_values("Menu",ascending=True)

# 3.Output
print(f'#1 -> Count:{numberOfItems}')
print(f'#2 {sorted_data}')