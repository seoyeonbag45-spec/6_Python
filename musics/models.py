class Music:
    """음악 공통 부모 클래스"""

    def __init__(self, music_id, title, artist, duration):
        self.music_id = music_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print("음악을 재생합니다.")

    def __str__(self):
        return (
            f"ID: {self.music_id}, "
            f"제목: {self.title}, "
            f"아티스트: {self.artist}, "
            f"재생시간: {self.duration}초"
        )


class Song(Music):
    """노래 클래스"""

    def __init__(self, music_id, title, artist, duration, lyrics):
        super().__init__(music_id, title, artist, duration)
        self.lyrics = lyrics

    def play(self):
        print(f"{self.lyrics}와 함께 음악 재생")

    def __str__(self):
        return (
            f"[노래] {super().__str__()}, "
            f"가사: {self.lyrics}"
        )