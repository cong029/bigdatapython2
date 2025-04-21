import random

# 노래 리스트 예시
songs = {
    "아이유": ["좋은 날", "밤편지", "꽃갈피"],
    "방탄소년단": ["Dynamite", "Butter", "FAKE LOVE"],
    "블랙핑크": ["How You Like That", "DDU-DU DDU-DU", "Lovesick Girls"],
    "엑소": ["Love Shot", "Tempo", "Power"]
}

# 메뉴 출력 함수
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

# 가수 이름으로 노래 리스트 출력 함수
def search_by_artist():
   
