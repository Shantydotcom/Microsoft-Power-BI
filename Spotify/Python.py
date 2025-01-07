import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load your dataset 
# Update with your file path
data = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

# Spotify API credentials
client_id = '842202d6cc3144b1a4c307860722f392'  # Replace with your Spotify Client ID
client_secret = '3beb286a49b8434aafd93a23061ef31e'  # Replace with your Spotify Client Secret

# Authenticate with Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to fetch album cover URL
def fetch_album_cover(track_name, artist_name):
    try:
        # Search for the track on Spotify
        results = sp.search(q=f"track:{track_name} artist:{artist_name}", type='track', limit=1)
        if results['tracks']['items']:
            album_cover_url = results['tracks']['items'][0]['album']['images'][0]['url']
            return album_cover_url
        else:
            return None
    except Exception as e:
        print(f"Error fetching data for {track_name} by {artist_name}: {e}")
        return None

# Add a new column for album cover URLs
data['album_cover_url'] = data.apply(
    lambda row: fetch_album_cover(row['track_name'], row['artist(s)_name']), axis=1
)

# Save the updated dataset
output_file = 'spotify-2023-with-covers.csv'
data.to_csv(output_file, index=False, encoding='utf-8')
print(f"Updated dataset saved to {output_file}")
