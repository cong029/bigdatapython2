import random

# 노래 리스트
songs = ["A노래", "B노래", "C노래", "D노래"]

def 추천곡():
    print("제가 추천할 노래는:")
    추천곡 = random.choice(songs)
    print(f"추천 노래: {추천곡}")

def 노래리스트():
    print("현재 노래 리스트:")
    for song in songs:
        print(song)

# 메뉴 선택
print("1. 노래 리스트 보기")
print("2. 노래 추천 받기")
선택 = input("메뉴를 선택하세요: ")

if 선택 == "1":
    노래리스트()
elif 선택 == "2":
    추천곡()
else:
    print("잘못된 입력입니다.")
