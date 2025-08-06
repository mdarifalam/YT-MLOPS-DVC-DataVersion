import pandas as pd
import os


data = {'Name': [ 'sunil','raunak','shashi'],
        'Age': [20,26,29],
        'city': ['patna','baliya', 'rohtas']
        }

df = pd.DataFrame(data)


data_dir = 'data'

os.makedirs(data_dir, exist_ok = True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")