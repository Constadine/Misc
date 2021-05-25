from random import randrange


class Video:
    def __init__(self, artist, title, duration) -> None:
        self.artist = artist
        self.title = title
        self.duration = duration

    def __str__(self) -> str:
        return f"{self.artist} - {self.title} ({self.duration})"


class Playlist:
    def __init__(self, title, description, duration, videos=None) -> None:
        self.title = title
        self.description = description
        self.duration = duration
        if videos is None:
            self.videos = []
        else:
            self.videos = videos

    def __str__(self) -> str:
        st = f"\nPlaylist: {self.title} ({self.description}). Duration: {self.duration}"
        for video in self.videos:
            st += "\n" + str(video)

        return st

    def add_video(self, video):
        self.videos += [video]

    def recommendation(self):
        return f"Recommended: {self.videos[randrange(len(self.videos))]}"


class Classical_Playlist(Playlist):
    def __init__(self, title, description, duration, videos, period) -> None:
        super().__init__(title, description, duration, videos=videos)
        self.period = period

    def recommendation(self):
        return f"Recommended: {self.videos[0]}"
