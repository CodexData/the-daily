from GoogleNews import GoogleNews
import pandas as pd

class Scraper:
    print("What news are you looking for? ")
    news_in = input()
    news = GoogleNews(period='1d')
    news.search(news_in)
    result = news.result()
    data = pd.DataFrame.from_dict(result)
    data = data.drop(columns=["img"])
    print(data)

if __name__ == "__main__":
    Scraper
