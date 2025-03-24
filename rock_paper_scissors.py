import random

def rock_paper_scissors():
    choices = ["가위", "바위", "보"]
    computer = random.choice(choices)
    user = input("가위, 바위, 보 중 하나를 선택하세요: ")

    if user not in choices:
        print("올바른 입력이 아닙니다. '가위', '바위', '보' 중에서 선택하세요.")
        return

    print(f"컴퓨터: {computer}, 당신: {user}")

    if user == computer:
        print("비겼습니다!")
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        print("이겼습니다!")
    else:
        print("졌습니다!")

rock_paper_scissors()

