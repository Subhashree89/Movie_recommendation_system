import streamlit as st
import pickle as pk
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b057f1f46d2323cb8919630cf8ef266a&language=en-US'.format(movie_id))
    data = response.json()
    full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    #return "https://image.tmdb.org/t/p/w500/[poster_path]"
    return full_path

def reccomend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recomended_movies=[]
    recomended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch api for posters
        recomended_movies.append(movies.iloc[i[0]].title)
        recomended_movies_posters.append(fetch_poster(movie_id))
    return recomended_movies,recomended_movies_posters

movies_dict = pk.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pk.load(open('similarity.pkl','rb'))

st.title('Movie recomender system')
selected_movie_name=st.selectbox('select your movies',movies['title'].values)

if st.button('reccomend'):
    names,posters = reccomend(selected_movie_name)
    col1, col2, col3, col4 = st.columns(4)
       
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])   
    with col4:
        st.text(names[3])
        st.image(posters[3])
        




