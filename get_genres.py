###### Doesn't work with wholfe file as written
###### too big for spotify's API, need to look into batching it

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np 

# Import history as csv file, create string column to 

df = pd.read_csv('/Users/michaelrozewski/Desktop/Spotify Extended Streaming History/Streaming_History_Audio_2022-2023_10.csv', encoding='utf-8')

sample_df['master_metadata_album_artist_name'] = df['master_metadata_album_artist_name'].astype(str).replace('nan', np.nan)

print(sample_df)

# Authenticate
client_id = ''
client_secret = ''
uri = 'http://localhost'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

for artist_name in sample_df['master_metadata_album_artist_name']:

    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = sample_df['master_metadata_album_artist_name']
    
sample_df['genre'] = sp.search(search_str)

df['seconds']= df['ms_played'] / 1000

df = pd.read_csv('/Users/michaelrozewski/Desktop/Spotify Extended Streaming History/Streaming_History_Audio_2022-2023_10.csv')



