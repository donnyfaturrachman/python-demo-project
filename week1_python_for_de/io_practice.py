# - Gunakan open(), csv, json, dan pandas.read_csv().
# - Baca file sales.csv, tampilkan 5 baris pertama.
# - Tulis ulang ke sales_copy.csv.

import pandas as pd

# Baca file sales.csv
df = pd.read_csv('/home/master/github/python-demo-project/week1_python_for_de/data/sales_raw.csv')
print(df.head())

# Tulis ulang ke sales_copy.csv
df.to_csv('/home/master/github/python-demo-project/week1_python_for_de/data/sales_copy.csv', index=False)