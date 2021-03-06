import requests
import constants
import fetch_data
import spotifyauth

# Get user input:
print("Tell us the date for which you'd like to create a playlist for!")
user_date = input("Enter the date in YYYY-MM-DD format:")
year_entered = user_date.split("-")[0]

# Fetch data from Billboards:
user_choice_urL = constants.BASE_BILLBOARDS_URL + user_date
billboards_response = requests.get(user_choice_urL)

# Get Top 100 songs and their Spotify IDs:
top_100_songs = fetch_data.get_top_100_songs(billboards_response)
songs_resource_id = fetch_data.get_songs_uri(top_100_songs, year_entered)

# Create a playlist:
user_id = spotifyauth.getUserId()
new_playlist = spotifyauth.sp.user_playlist_create(user=user_id,
                                    name=f"Top 100 Hits from {year_entered}",
                                    public=True,
                                    description=f"Billboard's Hot 100 hit songs on {user_date}"
                                  )

#Last step:Add your songs!
spotifyauth.sp.playlist_add_items(playlist_id = new_playlist["id"], items = songs_resource_id)
