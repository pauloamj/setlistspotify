import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

class SpotifyAPI:
    def __init__(self) -> None:
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

        # Authorization scopes to define permissions
        self.scope = 'playlist-modify-private,playlist-modify-public'
        # User authorization
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri, scope=self.scope))
        self.user_id = self.sp.me()['id']

    def get_track_uri(self, track, artist):
        results = self.sp.search(q=f'{track} {artist}', type='track')
        if len(results['tracks']['items']) > 0:
            return results['tracks']['items'][0]['uri']
        else:
            return None

    def create_playlist(self, info):
        playlist_name = f"{info['artist']} @ {info['venue']} | {info['date']}"
        print("Creating playlist...")
        playlist = self.sp.user_playlist_create(user=self.user_id, name=playlist_name, public=True, description="Created from the setlist")
        playlist_id = playlist["id"]
        return playlist_id

    def add_items_to_playlist(self, playlist_id, track_uris):
        print("Adding items to playlist...")
        return self.sp.playlist_add_items(playlist_id, track_uris)

    def get_track_uri_list(self, song_list, info):
        track_uris = []
        for song in song_list:
            uri = self.get_track_uri(song["name"], info["artist"])
            track_uris.append(uri)
        return track_uris

    def play(self, info, song_list):
        print("get tracks")
        track_uris = self.get_track_uri_list(song_list, info)
        print("create playlist")
        playlist_id = self.create_playlist(info)
        print("add items")
        response = self.add_items_to_playlist(playlist_id, track_uris)
        return response
    
