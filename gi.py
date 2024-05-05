from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_GI(food="bread"):

    request_json = f'1'                                                      #request_json = info from table based on name colmn

    GI_data = requests.get(request_json).json()

    return GI_data


if __name__ == "__main__":
    print('\n*** Get GI data ***\n')

    food = input("\nPlease eneter a food name:")

    GI_data = get_GI(food)

    print("\n")
    pprint(GI_data)                                                           #provide GI_data at the terminal

