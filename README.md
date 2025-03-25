## 🎧 MusicBrainz → Spotify Release Browser

**🔗 Live Demo:**  
[https://yogo9.github.io/Recent-Spotify-Releases/](https://yogo9.github.io/Recent-Spotify-Releases/)

This is a tool I use for myself to get the latest Spotify releases from an artist collection I maintain in [MusicBrainz](https://musicbrainz.org).

---

### 🔁 How it works

1. Use the script:
   ```bash
   python musicbrainz_spotify_export.py <collection URL>
   ```
   This will create a `spotify_urls.txt` file with Spotify artist URLs pulled from the MusicBrainz collection.

2. Open the web app (included in this repo) and paste in the list of Spotify URLs.

3. The app will fetch the latest **albums and singles** from those artists, and display them in a clean, sortable grid.

4. You’ll have the option to **submit each release to MusicBrainz** via [Harmony](https://harmony.pulsewidth.org.uk).
