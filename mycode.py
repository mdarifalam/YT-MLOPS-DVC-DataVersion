import pandas as pd
import os

data = {'Name': ['sunil', 'raunak', 'shashi'],
        'Age': [20, 26, 29],
        'city': ['patna', 'baliya', 'rohtas']}

df = pd.DataFrame(data)

# Corrected new_row keys
new_row = {'Name': 'Rohan', 'Age': 27, 'city': 'bihiya'}

# Append using loc or concat
df.loc[len(df)] = new_row

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
