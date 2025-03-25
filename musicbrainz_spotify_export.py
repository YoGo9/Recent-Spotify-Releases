import requests
import time
import sys
from urllib.parse import urlparse

def extract_collection_id(url):
    parts = urlparse(url)
    if "musicbrainz.org" not in parts.netloc or not parts.path.startswith("/collection/"):
        raise ValueError("Invalid MusicBrainz collection URL.")
    return parts.path.split("/")[-1]

def get_artist_mbid_list(collection_id):
    artists = []
    offset = 0
    limit = 100
    headers = {
        "User-Agent": "SpotifyURLFetcher/1.0 (your@email.com)"
    }

    while True:
        res = requests.get(f"https://musicbrainz.org/ws/2/collection/{collection_id}/artists",
                           params={"fmt": "json", "limit": limit, "offset": offset},
                           headers=headers)
        if res.status_code != 200:
            raise Exception(f"Error fetching collection: {res.status_code}")
        data = res.json()
        artists.extend(data.get("artists", []))
        if offset + limit >= data.get("artist-count", 0):
            break
        offset += limit
        time.sleep(1)
    return artists

def get_spotify_url(mbid):
    headers = {
        "User-Agent": "SpotifyURLFetcher/1.0"
    }
    res = requests.get(f"https://musicbrainz.org/ws/2/artist/{mbid}",
                       params={"fmt": "json", "inc": "url-rels"},
                       headers=headers)
    if res.status_code != 200:
        return None
    data = res.json()
    for rel in data.get("relations", []):
        url = rel.get("url", {}).get("resource", "")
        if "spotify.com" in url:
            return url
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python musicbrainz_spotify_export.py <collection_url>")
        sys.exit(1)

    collection_url = sys.argv[1]

    try:
        collection_id = extract_collection_id(collection_url)
        print("Fetching artist list...")
        artists = get_artist_mbid_list(collection_id)
        print(f"Found {len(artists)} artists.")

        spotify_urls = []
        for i, artist in enumerate(artists, 1):
            mbid = artist["id"]
            spotify_url = get_spotify_url(mbid)
            if spotify_url:
                print(f"[{i}/{len(artists)}] {artist['name']} → {spotify_url}")
                spotify_urls.append(spotify_url)
            else:
                print(f"[{i}/{len(artists)}] {artist['name']} → No Spotify link found.")
            time.sleep(1)

        with open("spotify_urls.txt", "w", encoding="utf-8") as f:
            for url in spotify_urls:
                f.write(url + "\n")

        print(f"\nDone! {len(spotify_urls)} Spotify artist URLs saved to spotify_urls.txt")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
