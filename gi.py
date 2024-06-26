import json
from pprint import pprint
import requests
import os

# Load the JSON data
with open('static/styles/Gtable.json', 'r') as json_file:
    data = json.load(json_file)

def get_GI(Food):
   
    for row in data:
        if row['Food'].lower() == Food.lower():
            GI_data = {'Food': Food, 'GI': row["GI"], 'GL': row["GL"], 'Carb': row["Carb"] }
            return GI_data
    return None


if __name__ == "__main__":
    print('\n*** Get GI data ***\n')

    food = input("\nPlease eneter a food name:")

    # check for empty strings of string with only space
    if not bool(food.strip()):
        food = "Milky Way bar"

    GI_data = get_GI(food)

    print("\n")
    pprint(GI_data)                                                           #provide GI_data at the terminal

