import random

# 노래 리스트
songs = {
    "아이유": ["좋은 날", "밤편지", "꽃갈피"],
    "방탄소년단": ["Dynamite", "Butter", "FAKE LOVE"],
    "블랙핑크": ["How You Like That", "DDU-DU DDU-DU", "Lovesick Girls"],
    "엑소": ["Love Shot", "Tempo", "Power"]
}

# 메뉴 출력
def print_menu():
    print("===================")
    print("1. 멜론 100")
    print("2. 멜론 50")
    print("3. 멜론 10")
    print("4. AI 추천 노래")
    print("5. 가수 이름 검색")
    print("===================")

# 노래 추천 함수
def recommend_song():
    song_list = sum(songs.values(), [])  # 모든 노래 리스트 합치기
    recommended_song = random.choice(song_list)
    print(f"추천 노래: {recommended_song}")

# 가수 이름으로 노래 리스트 출력
def search_by_artist():
    artist = input("가수 이름을 입력하세요: ")
    if artist in songs:
        print(f"{artist}의 노래 리스트:")
        for song in songs[artist]:
            print(f"- {song}")
    else:
        print(f"{artist}의 노래는 찾을 수 없습니다.")

# 메뉴 선택 및 실행
def menu_select():
    while True:
        print_menu()
        n = input("메뉴선택(1~5): ")

        if n == "1":
            print("멜론 100 차트")
        elif n == "2":
            print("멜론 50 차트")
        elif n == "3":
            print("멜론 10 차트")
        elif n == "4":
            recommend_song()
        elif n == "5":
            search_by_artist()
        else:
            print("잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")
            continue  # 잘못된 입력은 다시 메뉴로 돌아가게 함

# 프로그램 실행
menu_select()
