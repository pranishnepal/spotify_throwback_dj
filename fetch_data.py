from contracts import contract
from requests import Response
import constants
from spotifyauth import sp as spotify
from bs4 import BeautifulSoup

@contract(billboards_response=Response, returns ='list[>=0](str)')
def get_top_100_songs(billboards_response):
    """
    :param billboards_response: Response object
    :return: str: a list of top 100 songs
    """
    soup = BeautifulSoup(billboards_response.text, "html.parser")
    songs_html_elements = soup.find_all("span", class_=constants.SONG_CLASS_NAME)
    top_100_songs = [song.get_text() for song in songs_html_elements]
    return top_100_songs

@contract(top_100_songs = 'list(str)', year_entered = str, returns = "list(str)")
def get_songs_uri(top_100_songs, year_entered):
    """
    :param top_100_songs: list: a list of top 100 songs
    :param year_entered: str: user entered year
    :return: list: a list of URI's of `top_100_songs`
    """
    songs_URI = []
    for song in top_100_songs:
        response = spotify.search(q=f"track:{song} year:{year_entered}", type=["track"])
        try:
            song_uri = response["tracks"]["items"][0]["uri"]
            songs_URI.append(song_uri)
        except Exception:
            print(f"Song << {song} >> not found ://")

    return songs_URI
