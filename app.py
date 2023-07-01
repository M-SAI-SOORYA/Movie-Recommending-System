import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
       response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b06f5ab31c81a66c57e1ab13303f0cc8'.format(movie_id))
       data=response.json()
       return "https://image.tmdb.org/t/p/w200/"+data['poster_path']
def fetch_vote_average(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b06f5ab31c81a66c57e1ab13303f0cc8'.format(movie_id))
    data=response.json()
    return data['vote_average']
st.title("BEST Movies For You!")
movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
selected_movie_name=st.selectbox('Come on Lets Enjoy ! Tell your Movie',movies['title'].values)
st.image(fetch_poster(movies.iloc[movies[movies['title']==selected_movie_name].index[0]].id))

st.text("Rating:"+str(round(fetch_vote_average(movies.iloc[movies[movies['title']==selected_movie_name].index[0]].id)*10,1))+"%")

similarity=pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_listk=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  l=[]
  l1=[]
  l2=[]
  for i in movies_listk:
    movie_id=movies.iloc[i[0]].id
    l.append(movies.iloc[i[0]].title)
    l1.append(fetch_poster(movie_id))
    l2.append(fetch_vote_average(movie_id))
  return l,l1,l2
if (st.button('Recommend')):
    
    names,posters,popularity=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
        st.text("Rating:"+str(round(popularity[0]*10,1))+"%")
    with col2:
        st.text(names[1])
        st.image(posters[1])
        st.text("Rating:"+str(round(popularity[1]*10,1))+"%")
    with col3:
        st.text(names[2])
        st.image(posters[2])
        st.text("Rating:"+str(round(popularity[2]*10,1))+"%")
    with col4:
        st.text(names[3])
        st.image(posters[3])
        st.text("Rating:"+str(round(popularity[3]*10,1))+"%")
    with col5:
        st.text(names[4])
        st.image(posters[4])
        st.text("Rating:"+str(round(popularity[4]*10,1))+"%")
    

