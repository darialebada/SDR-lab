from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import AddItemProperty
from dotenv import load_dotenv
import os

load_dotenv()
DB_ID = os.getenv("RECOMBEE_DB_ID")
REGION = os.getenv("RECOMBEE_REGION")
TOKEN = os.getenv("RECOMBEE_PRIVATE_TOKEN")

client = RecombeeClient(DB_ID, TOKEN)

# send item properties
client.send(AddItemProperty("series_title", "string"))
client.send(AddItemProperty("released_year", "int"))
client.send(AddItemProperty("certificate", "string"))
client.send(AddItemProperty("runtime", "string"))
client.send(AddItemProperty("imdb_rating", "double"))
client.send(AddItemProperty("genre", "set"))
client.send(AddItemProperty("overview", "string"))
client.send(AddItemProperty("meta_score", "int"))
client.send(AddItemProperty("director", "string"))
client.send(AddItemProperty("star1", "string"))
client.send(AddItemProperty("star2", "string"))
client.send(AddItemProperty("star3", "string"))
client.send(AddItemProperty("star4", "string"))
client.send(AddItemProperty("no_of_votes", "int"))
client.send(AddItemProperty("gross", "string"))
