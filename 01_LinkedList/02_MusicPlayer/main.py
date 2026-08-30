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
    3,
    "Itni Si Baat Hain",
    "Armaan Malik",
    "Divide",
    "4:23",
    "music/song3.mp3"
)

music4 = Music(
    4,
    "Husn",
    "Anuv Jain",
    "Husn",
    "3:37",
    "music/song4.mp3"
)

music5 = Music(
    5,
    "Tum Se Hi",
    "Mohit Chauhan",
    "Jab We Met",
    "5:21",
    "music/song5.mp3"
)

music6 = Music(
    6,
    "Agar Tum Saath Ho",
    "Alka Yagnik, Arijit Singh",
    "Tamasha",
    "5:41",
    "music/song6.mp3"
)

music7 = Music(
    7,
    "Chaleya",
    "Arijit Singh, Shilpa Rao",
    "Jawan",
    "3:20",
    "music/song7.mp3"
)

music8 = Music(
    8,
    "Apna Bana Le",
    "Arijit Singh",
    "Bhediya",
    "4:21",
    "music/song8.mp3"
)

music9 = Music(
    9,
    "Kesariya",
    "Arijit Singh",
    "Brahmāstra",
    "4:28",
    "music/song9.mp3"
)

music10 = Music(
    10,
    "Heeriye",
    "Jasleen Royal, Arijit Singh",
    "Heeriye",
    "3:14",
    "music/song10.mp3"
)

music11 = Music(
    11,
    "Maan Meri Jaan",
    "King",
    "Champagne Talk",
    "4:24",
    "music/song11.mp3"
)

music12 = Music(
    12,
    "Satranga",
    "Arijit Singh",
    "Animal",
    "4:31",
    "music/song12.mp3"
)

music13 = Music(
    13,
    "O Maahi",
    "Arijit Singh",
    "Dunki",
    "3:53",
    "music/song13.mp3"
)

music14 = Music(
    14,
    "Iktara",
    "Kavita Seth",
    "Wake Up Sid",
    "4:13",
    "music/song14.mp3"
)

music15 = Music(
    15,
    "Kho Gaye Hum Kahan",
    "Jasleen Royal, Prateek Kuhad",
    "Kho Gaye Hum Kahan",
    "3:39",
    "music/song15.mp3"
)
#Add music to playlist
playlist.add_music(music1)
playlist.add_music(music2)
playlist.add_music(music3)
playlist.add_music(music4)
playlist.add_music(music5)

#Display Playlist
total = playlist.count()
print(f"{total} Music Tracks")
playlist.display_playlist()

#Remove song from playlist
playlist.remove_music(music4)

#Move song inside playlist

playlist.change_position(music5, music1)

playlist.display_playlist()


