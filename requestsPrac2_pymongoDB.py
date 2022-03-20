import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.6pe7g.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

#마치 사람이 요청을 날린 것 처럼 보여주기 위해 사용, 브라우저에서 요청한 것처럼됨. (실제론 코드에서 날림)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#구조를 먼저 파악해보기.
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(4) > td.title > div > a

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1) > img

#old_content > table > tbody > tr:nth-child(2) > td.point

movies = soup.select('#old_content > table > tbody > tr')

print(movies)

for movie in movies:
    title_tag = movie.select_one('td.title > div > a')
    rank_tag = movie.select_one('img')
    star_tag = movie.select_one('td.point')
    if title_tag is not None:
        title = title_tag.text
        rank = rank_tag['alt']
        star = star_tag.text
        doc = {
            'title': title,
            'rank' : rank,
            'star' : star
        }
        db.movies.insert_one(doc)
