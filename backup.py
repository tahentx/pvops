import pandas as pd
from haversine import haversine, Unit
df = pd.read_csv('tucson.csv')
lat,long = df['Lat '],df['Long']
print(lat[0])
