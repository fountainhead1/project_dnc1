import pandas as pd
import requests
from bs4 import BeautifulSoup
from src.service_news import get_news


# 뉴스 수집(Python) → Pandas DataFrame → Excel 저장


def news_collector(category, page = 1, count = 1):  # 사용자가 page / count값을 입력하지 않은 경우 자동으로 page와 count값이 자동으로 1이 됨
    collect_list = []  # 향후 데이터프레임 변환용

    while True:
        # 실습용(일단 2페이지까지만 수집하도록)
        if page == 3:
            break
        url = f"https://news.daum.net/breakingnews/{category}?page={page}"
        result = requests.get(url)

        if result.status_code == 200:
            print(result, "접속 성공 → 데이터를 수집합니다.")

            doc = BeautifulSoup(result.text, "html.parser")
            url_list = doc.select("ul.list_news2 a.link_txt")

            if len(url_list) == 0:
                break
            for url in (url_list):
               count += 1
               print(f"{count}.", "=" * 100)
               data = get_news(url["href"], category)
               collect_list.append(data)
        else:
            print("URL 경로가 잘못되었습니다.")

        page += 1
    #  뉴스 수집 완료
    #  - collect_list에 있는 것을 dataframe으로
    col_name = ["category", "title", "content", "date"]
    df_review = pd.DataFrame(collect_list, columns=col_name)

    return df_review, count  # tuple 타입으로 저장