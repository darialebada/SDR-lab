from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import SetItemValues, AddUserProperty, SetUserValues
from dotenv import load_dotenv
import names
import random
import pandas as pd
import os

load_dotenv()
DB_ID = os.getenv("RECOMBEE_DB_ID")
REGION = os.getenv("RECOMBEE_REGION")
TOKEN = os.getenv("RECOMBEE_PRIVATE_TOKEN")

client = RecombeeClient(DB_ID, TOKEN)

def add_items():
    df = pd.read_csv("imdb_top_1000.csv")

    for index, row in df.iterrows():
        item_id = str(index)
        item = {
            'series_title': row['Series_Title'],
            'released_year': int(row['Released_Year']),
            'certificate': row['Certificate'],
            'runtime': int(row['Runtime'].split(' ')[0]),
            'imdb_rating': float(row['IMDB_Rating']),
            'genre': set(row['Genre'].split(', ')),
            'overview': row['Overview'],
            'meta_score': float(row['Meta_score']),
            'director': row['Director'],
            'star1': row['Star1'],
            'star2': row['Star2'],
            'star3': row['Star3'],
            'star4': row['Star4'],
            'no_of_votes': int(row['No_of_Votes']),
            'gross': float(row['Gross'].replace(',', '')) if pd.notna(row['Gross']) else 0.0
        }
        client.send(SetItemValues(item_id, item, cascade_create=True))

def add_user_ids():
    for user_id in range(1, 31):
        client.send(SetUserValues(str(user_id), {}, cascade_create=True))

def add_user_properties():
    client.send(AddUserProperty("first_name", "string"))
    client.send(AddUserProperty("last_name", "string"))
    client.send(AddUserProperty("email", "string"))


def add_user_data():
    for user_id in range(1, 31):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': first_name.lower() + "."  + last_name.lower() + "@example.com",
        }
        client.send(SetUserValues(str(user_id), user_data, cascade_create=True))



if __name__ == '__main__':
    add_items()
    add_user_ids()
    add_user_properties()
    add_user_data()


