from email import header
from urllib import request
from dotenv import load_dotenv
import requests
import os

load_dotenv()

class SpotifyAPI:
    def __init__(self) -> None:
        self.user_id = os.getenv('SPOTIFY_USER_ID')
        self.access_token = os.getenv('SPOTIFY_ACCESS_TOKEN')
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def get_track_uri(self, track, artist):
        url = 'https://api.spotify.com/v1/search'
        params = {
            "q": f"{track} {artist}",
            "type": "track"
        }
        print(f"Searching {track} by {artist}...")
        r = requests.request("GET", url=url, headers=self.headers, params=params)
        return r.json()["tracks"]["items"][0]["uri"]
    
    def create_playlist(self, info):
        url = f'https://api.spotify.com/v1/users/{self.user_id}/playlists'
        json = {
            "name": f"{info['artist']} @ {info['venue']} | {info['date']}",
            "public": "false"
            }
        print("Creating playlist...")
        r = requests.request("POST", url=url, json=json, headers=self.headers)
        playlist_id =  r.json()["id"]
        return playlist_id
    
    def add_items_to_playlist(self, playlist_id, track_uris):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        json = {
            "uris": track_uris
        }
        print("Adding items to playlist...")
        return requests.request("POST", url=url, json=json, headers=self.headers)
        

    def get_track_uri_list(self, song_list, info):
        track_uris = []
        for song in song_list:
            uri = self.get_track_uri(song["name"], info["artist"])
            track_uris.append(uri)
        return track_uris
    
    def play(self, info, song_list):
        playlist_id = self.create_playlist(info)
        track_uris = self.get_track_uri_list(song_list, info)
        response = self.add_items_to_playlist(playlist_id, track_uris)
        return response