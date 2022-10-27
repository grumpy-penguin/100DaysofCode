# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temparatures = []
#     clean_data = iter(data)
#     next(clean_data)
#     for row in clean_data:
#         temparatures.append(int(row[1]))
#     print(temparatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # average = sum(data["temp"].to_list()) / len(data["temp"].to_list())
# # print(f"The average is: {int(data['temp'].mean())}")
# # print(f"The max value is: { data['temp'].max() }")
# # row = data[data.temp == data.temp.max()]
# # print(row)

# def conver_temp_to_farenheight(temp):
#     farenheight = temp * 1.8 + 32
#     return float(farenheight)

# new_temp = data.temp.apply(conver_temp_to_farenheight)
# print(new_temp)

# dict_student = {
#     "students": ["Amy", "James","Angela"],
#     "scores": [76, 56, 65]
# }

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colour = squirrel_data["Primary Fur Color"].value_counts()
squirrel_dict = squirrel_colour.to_dict()

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_colour.csv")



# with open("squirrel_colour_count.csv", mode="w") as file:
#     file.write(squirrel_colour.to_csv())
