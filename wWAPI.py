import requests
import pandas as pd

response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=99fb812beef447abe0a6c14a6dc48884&language=en-US&page=1")
#api_key = 99fb812beef447abe0a6c14a6dc48884

pd.DataFrame(response.json()['results'].head(2)[['id','tittle','overview','release_date','popularity','vote_average','vote_count']])
#response.json()['results']

df = pd.DataFrame()

#making a loop
for i in range(1,429):
    response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=99fb812beef447abe0a6c14a6dc48884&language=en-US&page=1")
    temp_df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
    df = pd.concat([df, temp_df], ignore_index=True)

df.to_csv('movies.csv')