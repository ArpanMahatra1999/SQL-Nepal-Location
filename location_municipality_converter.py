import pandas as pd

df = pd.read_csv("location_municipality.csv")
list_of_municipalities_with_name = list(df['name'])
list_of_municipalities_with_district_id = list(df['district_id'])
f = open('location_municipality', 'w')
f.write("INSERT INTO location_municipality(id, name, district_id)\nVALUES")
for l in range(0,len(list_of_municipalities_with_name)):
    f.write(f"({l+1}, '{list_of_municipalities_with_name[l]}',{list_of_municipalities_with_district_id[l]}),\n")
f.close()