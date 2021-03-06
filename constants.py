from dotenv import load_dotenv, find_dotenv
import os

#load .env file
load_dotenv(find_dotenv())

# load API keys:
load_dotenv(find_dotenv())
YOUR_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
YOUR_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIFY_SCOPE = "playlist-modify-public"
REDIRECT_URL_TO_EXAMPLE_DOT_COM = "http://example.com"

#Billboards URL and Web-Scrapped Class
BASE_BILLBOARDS_URL = "https://www.billboard.com/charts/hot-100/"
SONG_CLASS_NAME = "chart-element__information__song text--truncate color--primary"

#SPOTIFY search query:
SEARCH_QUERY = "tracks"
SEARCH_TYPE_LIST = ["track"]