import netCDF4
import re
import pandas as pd
import os

rows = list()
for fname in sorted(list(os.listdir('.'))):
    if not fname.endswith('.nc'):
        continue

    row = {'data_fname' : fname}
    with netCDF4.Dataset(fname) as nc:
        for aname in nc.ncattrs():
            row[aname] = nc.getncattr(aname)

    print(row['popular_name'])
    rows.append(row)

df = pd.DataFrame(data=rows)
print(df.columns)
df = df.sort_values(['glacier_number'])
df.to_csv('index.csv')
df.to_pickle('index.df')

