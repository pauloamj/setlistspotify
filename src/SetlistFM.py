import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()

SETLIST_KEY = os.getenv("setlist_key")

class SetlistFM:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json',
            'x-api-key': SETLIST_KEY
        }
    
    def get_setlist_object(self, id):
        url = "https://api.setlist.fm/rest/1.0/setlist/" + id
        r = requests.request(method="GET", url=url, headers=self.headers)
        return r.json()
    
    def get_id_from_url(self, url):
        return re.split("([a-zA-Z0-9]+)(?:(\.html*)?)$", url, 1)[1]

    def get_song_list(self, setlist:dict):
        song_list = []
        for set in setlist["sets"]["set"]:
            song_list += set["song"]
        return song_list

    def get_setlist_info(self, setlist:dict):
        setlist_info = {
            "artist": setlist['artist']['name'],
            "venue": setlist['venue']['name'],
            "date": setlist['eventDate']
        }
        return setlist_info

    def play(self, url):
        id = self.get_id_from_url(url)
        setlist = self.get_setlist_object(id)
        song_list = self.get_song_list(setlist)
        setlist_title = self.get_setlist_info(setlist)
        return setlist_title, song_list