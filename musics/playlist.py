from models import Song


class SongNotFoundError(Exception):
    """존재하지 않는 곡 ID 예외"""

    def __init__(self, music_id):
        super().__init__(
            f"ID {music_id}에 해당하는 곡이 없습니다."
        )


class DuplicateSongError(Exception):
    """중복 곡 등록 예외"""

    def __init__(self, title, artist):
        super().__init__(
            f"{artist}의 '{title}'은 이미 등록되어 있습니다."
        )


class Playlist:

    def __init__(self):
        self.music_list = []
        self.next_id = 1

    # 중복 검사
    def check_duplicate(self, title, artist):
        for music in self.music_list:
            if music.title == title and music.artist == artist:
                raise DuplicateSongError(title, artist)

    # 노래 등록
    def add_song(self, title, artist, duration, lyrics):

        self.check_duplicate(title, artist)

        song = Song(
            self.next_id,
            title,
            artist,
            duration,
            lyrics
        )

        self.music_list.append(song)
        self.next_id += 1

        print("노래가 등록되었습니다.")

    # 전체 조회
    def show_all(self):

        if not self.music_list:
            print("등록된 곡이 없습니다.")
            return

        for music in self.music_list:
            print(music)

    # ID 검색
    def find_by_id(self, music_id):

        for music in self.music_list:
            if music.music_id == music_id:
                return music

        raise SongNotFoundError(music_id)

    # 아티스트 검색
    def search_by_artist(self, artist):

        result = []

        for music in self.music_list:
            if artist.lower() in music.artist.lower():
                result.append(music)

        return result

    # 노래 재생
    def play_music(self, music_id):

        music = self.find_by_id(music_id)
        music.play()

    # 총 재생시간
    def get_total_duration(self):

        total = 0

        for music in self.music_list:
            total += music.duration

        return total

    # 노래 수정
    def update_music(self, music_id, title, duration):

        music = self.find_by_id(music_id)

        music.title = title
        music.duration = duration

        print("곡 정보가 수정되었습니다.")

    # 노래 삭제
    def delete_music(self, music_id):

        music = self.find_by_id(music_id)

        self.music_list.remove(music)

        print("곡이 삭제되었습니다.")