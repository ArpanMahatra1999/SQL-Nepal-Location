import pandas as pd

df = pd.read_csv("location_district.csv")
list_of_districts_with_name = list(df['name'])
list_of_districts_with_province_id = list(df['province_id'])
f = open('location_district', 'w')
f.write("INSERT INTO location_district(id, name, province_id)\nVALUES")
for l in range(0,len(list_of_districts_with_name)):
    f.write(f"({l+1}, '{list_of_districts_with_name[l]}',{list_of_districts_with_province_id[l]}),\n")
f.close()