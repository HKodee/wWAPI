import requests
import pandas as pd

response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=99fb812beef447abe0a6c14a6dc48884&language=en-US&page=1")
#api_key = 99fb812beef447abe0a6c14a6dc48884

pd.DataFrame(response.json()['results'].head(2)[['id','tittle','overview','release_date','popularity','vote_average','vote_count']])
#response.json()['results']

df= pd.DataFrame()

