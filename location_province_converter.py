import pandas as pd

df = pd.read_csv("location_province.csv")
list_of_provinces = list(df['name'])
f = open('location_province', 'w')
f.write("INSERT INTO location_province(id, name)\nVALUES")
for l in range(0,len(list_of_provinces)):
    f.write(f"({l+1},'{list_of_provinces[l]}'),\n")
f.close()