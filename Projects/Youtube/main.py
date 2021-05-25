from playlist_classes import Video, Playlist, Classical_Playlist
from random import seed
from datetime import datetime

seed(datetime.now())

videos = [Video("HIM", "Heartkiller", "03.23"), Video("HIM", "Bleed Well", "03.40"),
          Video("Poets of the fall", "Sweet escape", "05.23")]

my_playlist = Playlist("Love", "Songs that melt hearts", "10:01", videos)

print(my_playlist.recommendation())

another_him_video = Video("HIM", "The path", "08.37")

my_playlist.add_video(another_him_video)

print(my_playlist)
print(my_playlist.recommendation())

classic_playlist = Classical_Playlist(
    "My Classical Playlist", "Classic stuff", "14:21", [Video("Beethoven", "Track 01", "03:12"), Video("Beethoven", "Track 02", "04:26")], "baroque")

print(classic_playlist)
print(classic_playlist.recommendation())
