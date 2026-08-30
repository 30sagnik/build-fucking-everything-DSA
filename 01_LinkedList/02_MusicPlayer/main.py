from music import Music
from playlist import Playlist

playlist = Playlist()

music1 = Music(
    1,
    "Arz Kiya Hai",
    "Anuv Jain",
    "After Hours",
    "3:20",
    "music/song1.mp3"
)

music2 = Music(
    2,
    "Raabta",
    "Arijit Singh",
    "Divide",
    "4:23",
    "music/song2.mp3"
)

music3 = Music(
    2,
    "Itni si Baat Hain",
    "Armaan Malik",
    "Divide",
    "4:23",
    "music/song2.mp3"
)

playlist.add_music(music1)
playlist.add_music(music2)
playlist.add_music(music3)

playlist.display_playlist()

playlist.search("Ar")
