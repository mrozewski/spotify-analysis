###
### This should add genre as a field, but I think the request times out the API
### Maybe look into batching it
###

 # Import numpy for handling NaN values
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np 

# Authenticate
client_id = '6661850d662c497b865e74437faffdc6'
client_secret = '946539de52914494bc2aa3509a07f4aa'
uri = 'http://localhost'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Read the CSV file into a DataFrame
# Trim unecessary columns, lots of data


pre_df = pd.read_csv('/Users/michaelrozewski/Desktop/Spotify Extended Streaming History/Streaming_History_Audio_2022-2023_10.csv', encoding='utf-8')

df = pre_df[['master_metadata_track_name', 'master_metadata_album_artist_name','master_metadata_album_album_name']]

df.dropna()


genre_list = []
for artist_name in df['master_metadata_album_artist_name']:
    if pd.isna(artist_name):  # Check if artist_name is NaN
        genre_list.append(None)  # Append None if artist_name is NaN
    else:
        results = sp.search(q='artist:' + artist_name, type='artist')
        artists = results['artists']['items']
        if len(artists) > 0:
            artist = artists[0]
            genres = artist.get('genres', [])
            genre_list.append(genres[0] if genres else None)
        else:
            genre_list.append(None)

# Add the genre list as a new column 'genre' to the DataFrame
df['genre'] = genre_list

print(df[['master_metadata_album_artist_name', 'genre']].sample(20))
