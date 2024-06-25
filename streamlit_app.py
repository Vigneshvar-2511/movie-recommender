import streamlit as st
import pickle
import pandas as pd

def reccomend(movie):
    recc=[]
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        movie_id=i[0]
        recc.append(movies.iloc[i[0]].title)
    return recc



movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('simi.pkl','rb'))
st.title('Movie recommender system')
option = st.selectbox(
    "Select a movie",movies['title'].values)

if st.button("Reccomend",type="secondary"):
    st.write("You selected:", option)
    reccs=reccomend(option)
    for i in reccs:
        st.write(i)
