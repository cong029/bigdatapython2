import requests
from bs4 import BeautifulSoup

def main():
    # 네이버 블로그 인기글 페이지 URL
    url = 'https://section.blog.naver.com/'

    # 웹페이지 요청 보내기
    response = requests.get(url)

    # 응답이 잘 왔는지 확인
    if response.status_code == 200:
        # HTML 소스를 BeautifulSoup을 사용해 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 인기 글 제목 찾기
        titles = soup.find_all('a', {'class': 'link_tit'})  # 인기글 링크 클래스

        # 제목 출력하기
        for i, title in enumerate(titles):
            print(f"{i + 1}. {title.get_text()}")  # 글 제목만 출력
    else:
        print("웹 페이지를 불러오는 데 실패했습니다.")

# 프로그램 실행
if __name__ == "__main__":
    main()
