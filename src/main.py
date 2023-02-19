from SetlistFM import SetlistFM
from Spotify import SpotifyAPI

def main():
    setlist = SetlistFM()
    url = "https://www.setlist.fm/setlist/bruce-springsteen/2023/toyota-center-houston-tx-33bd4071.html"
    info, song_list = setlist.play(url)

    spotify = SpotifyAPI()
    r = spotify.play(info, song_list)
    print("Done!" if r.status_code < 400 else "Hmm something went wrong...")


if __name__ == "__main__":
    main()