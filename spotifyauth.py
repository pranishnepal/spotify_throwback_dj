import spotipy
import constants
from spotipy.oauth2 import SpotifyOAuth
from contracts import contract

#Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=constants.YOUR_CLIENT_ID,
        client_secret=constants.YOUR_CLIENT_SECRET,
        redirect_uri=constants.REDIRECT_URL_TO_EXAMPLE_DOT_COM,
        scope=constants.SPOTIFY_SCOPE,
        open_browser=True,
        show_dialog=True,
        cache_path="cachedData.txt"
    )
)

@contract(returns = str)
def getUserId():
    """
    :return: str: authenticated user's id
    """
    return sp.me()["id"]