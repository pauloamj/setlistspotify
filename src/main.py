from SetlistFM import SetlistFM
from Spotify import SpotifyAPI

def main():
    setlist = SetlistFM()
    url = "https://www.setlist.fm/setlist/the-linda-lindas/2023/mohawk-austin-tx-6bbdba92.html"
    info, song_list = setlist.play(url)
    spotify = SpotifyAPI()
    r = spotify.play(info, song_list)
    print("Done!" if r.status_code < 400 else "Hmm something went wrong...")
    print(r)


if __name__ == "__main__":
    main()