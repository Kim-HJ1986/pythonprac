from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.6pe7g.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

#가버나움의 평점 가져오기
movie = db.movies.find_one({'title':'가버나움'})
print(movie['star'])

#가버나움과 같은 평점의 영화 모두 가져오기
movie_list = list(db.movies.find({'star':movie['star']}, {'_id': False}))
for target_movie in movie_list:
    print(target_movie['title'])

#가버나움의 평점 0으로 바꾸기
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})