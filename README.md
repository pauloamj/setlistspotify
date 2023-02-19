Setlist Spotify
===============

This project is a Python script that takes a Setlist.fm URL and creates a Spotify playlist with the songs played at that concert.

Setup
-----

### Prerequisites

You need to have Docker and docker-compose installed on your machine.

### Installation

1. Clone this repository:

```bash
git clone https://github.com/pauloamj/setlist-spotify.git
cd setlist-spotify

```

2. Create a file named `.env` in the root directory with the following variables:

```
setlist_key=
SPOTIFY_ACCESS_TOKEN=
SPOTIFY_USER_ID=
```

To get a Setlist.fm API key, visit [setlist.fm](https://www.setlist.fm/settings/api).

To get a Spotify Access Token, go to the [Spotify Console](https://developer.spotify.com/console/post-playlist-tracks/) and click on the "Get Token" button.

To get your Spotify User ID, click on the share button on your Spotify profile, and copy the string of numbers in the URL.

3. Open `src/main.py` and replace the value of the `url` variable with the URL of the Setlist.fm page you want to create a playlist for.

4. Build the Docker container:

```bash
docker-compose build

```

5. Run the Docker container:

```bash
docker-compose up --force-recreate

```

This will build the Docker image and start the container.

The result will be a new Spotify playlist with the songs from the Setlist.fm page you specified that can be found in your Spotify APP.
