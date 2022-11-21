import json

f = open('data.json', encoding = "utf8")

data = json.load(f)

def Data():
    return data

# for i in data:
#     print(i["rest_id"])
#     print(i["Name"])
#     print(i["Location"])
#     print(i["Type_of_food"])
#     print(i["Recommend_menu"])
#     print(i["Opening-Closing_time"])
#     print(i["Contact_number"])
#     print()