import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#### get date from user and scrape billboard for top 100 songs
date = input("What year do you want to travel to? (YYYY-MM-DD)")
URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

all_songs_titles = soup.find_all(id='title-of-a-story', class_="c-title")

song_titles = [song.getText().strip() for song in all_songs_titles if song.parent.name == 'li']

#### make spotify playlist
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-public",
                                               cache_path='token.txt'))

# Get current user details
user = sp.current_user()
# print(user)
user_id = user["id"]
# print(user)

song_uri_list = []
for title in song_titles:
    try:
        result = sp.search(q='track:' + title, type='track', limit=1)
        if title in result['tracks']['items'][0]['name']:
            song_uri = result['tracks']['items'][0]['uri']
            song_uri_list.append(song_uri)
        else:
            print(f"{title}|||{result['tracks']['items'][0]['name']}")
    except:
        print("No song found for: " + title)

playlist_id = ""
try:
    playlist_name = f"Hot 100: {date}"
    response = sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=True,
        collaborative=False,
        description='Hot 100 from billboard.com'
    )
    print(response)
    playlist_id = response["id"]
except Exception as E:
    print(E)
finally:
    res = sp.playlist_add_items(playlist_id=playlist_id, items=song_uri_list)
    print(res)