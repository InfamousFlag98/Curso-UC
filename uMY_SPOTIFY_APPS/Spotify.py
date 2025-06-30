import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="09bc176f84244209be398249260411e3",
    client_secret="79feeb85be2949b18bc2bb91ae88ce8c",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-public playlist-modify-private"
))

# Your user ID
user_id = sp.current_user()["id"]

# Playlist name
playlist_name = "ALTERAR AQUI"

# Create playlist
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description="ALTERAR AQUI")
playlist_id = playlist["id"]

# List of track names
track_names = [
    
    # Add more here...
]

# Search and collect track URIs
track_uris = []
for track in track_names:
    results = sp.search(q=track, type="track", limit=1)
    if results["tracks"]["items"]:
        uri = results["tracks"]["items"][0]["uri"]
        track_uris.append(uri)

# Add tracks to playlist in chunks of 100
for i in range(0, len(track_uris), 100):
    sp.playlist_add_items(playlist_id, track_uris[i:i+100])

print(f"Playlist '{playlist_name}' created and synced!")
