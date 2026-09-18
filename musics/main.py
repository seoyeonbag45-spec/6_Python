from playlist import (
    Playlist,
    SongNotFoundError,
    DuplicateSongError
)


playlist = Playlist()


while True:

    print()
    print("=" * 40)
    print("음악 관리 프로그램")
    print("=" * 40)
    print("1. 노래 등록")
    print("2. 전체 조회")
    print("3. 노래 재생")
    print("4. 아티스트 검색")
    print("5. 총 재생시간 조회")
    print("6. 곡 수정")
    print("7. 곡 삭제")
    print("0. 종료")
    print("=" * 40)

    menu = input("메뉴 선택: ")

    try:

        # 1. 노래 등록
        if menu == "1":

            title = input("제목: ")
            artist = input("아티스트: ")
            duration = int(input("재생시간(초): "))
            lyrics = input("가사: ")

            playlist.add_song(
                title,
                artist,
                duration,
                lyrics
            )

        # 2. 전체 조회
        elif menu == "2":

            playlist.show_all()

        # 3. 노래 재생
        elif menu == "3":

            music_id = int(
                input("재생할 곡 ID: ")
            )

            playlist.play_music(music_id)

        # 4. 아티스트 검색
        elif menu == "4":

            artist = input("검색할 아티스트: ")

            result = playlist.search_by_artist(artist)

            if result:
                for music in result:
                    print(music)
            else:
                print("검색 결과가 없습니다.")

        # 5. 총 재생시간
        elif menu == "5":

            total = playlist.get_total_duration()

            print(f"총 재생시간: {total}초")

        # 6. 곡 수정
        elif menu == "6":

            music_id = int(
                input("수정할 곡 ID: ")
            )

            title = input("새 제목: ")

            duration = int(
                input("새 재생시간(초): ")
            )

            playlist.update_music(
                music_id,
                title,
                duration
            )

        # 7. 곡 삭제
        elif menu == "7":

            music_id = int(
                input("삭제할 곡 ID: ")
            )

            playlist.delete_music(music_id)

        # 0. 종료
        elif menu == "0":

            print("프로그램을 종료합니다.")
            break

        else:
            print("올바른 메뉴 번호를 입력해주세요.")

    except SongNotFoundError as e:
        print(e)

    except DuplicateSongError as e:
        print(e)

    except ValueError:
        print("숫자를 입력해주세요.")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")