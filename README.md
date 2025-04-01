## 🎧 MusicBrainz → Spotify Release Browser



This is a tool I use for myself to get the latest Spotify releases from an artist collection I maintain in [MusicBrainz](https://musicbrainz.org).

---

### 🔁 How it works

1. Use the script:
   ```bash
   python musicbrainz_spotify_export.py <collection URL>
   ```
   This will create a `spotify_urls.txt` file with Spotify artist URLs pulled from the MusicBrainz collection.

2. Download CSV from https://github.com/jakubito/spotify-release-list
