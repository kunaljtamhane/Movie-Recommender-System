import pickle
import streamlit as st
import requests
import pandas as pd

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=0f0f0acdbf17f1adaa37e96010a7ee67&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path



# def recommend(movie):
#     index = movies[movies['title']==movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#     return recommended_movie_names, recommended_movie_posters


# st.header("Movies Recommendation System using Machine Learning")
# movies = pickle.load(open('movie_dict.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))

# movie_list = movies['title'].values()

# selected_movie = st.selectbox(
#     'Type or select a movie to get recommendation',
#     movie_list
# )


# if st.button('Show recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])

#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
    
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])

#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])

#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])






#############################

# Function to fetch the poster and Google search URL of the movie
def fetch_poster_and_url(movie_id, movie_title):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3f63b8ac769f4634a544f33033e7a7fa&language=en-US'.format(movie_id))
    data = response.json()
    poster_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    google_search_url = f"https://www.google.com/search?q={movie_title.replace(' ', '+')}"
    return poster_url, google_search_url


# Function to recommend movies
def recommend(movie, movies_data):
    movie_index = movies_data[movies_data['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_ = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_urls = []
    for i in movies_list_:
        movie_id = movies_data.iloc[i[0]].movie_id
        movie_title = movies_data.iloc[i[0]].title
        poster_url, google_search_url = fetch_poster_and_url(movie_id, movie_title)
        recommended_movies.append(movie_title)
        recommended_movies_posters.append(poster_url)
        recommended_movies_urls.append(google_search_url)
    return recommended_movies, recommended_movies_posters, recommended_movies_urls


# Load the model and the movie list
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Which movie do you like best?',
    movies['title'].values)

if st.button('Recommend'):
    names, posters, urls = recommend(selected_movie_name, movies_data=movies)
    cols = st.columns(5) # 5 columns to display the recommendations

    for i, col in enumerate(cols):
        col.markdown(f"[{names[i]}]({urls[i]})")
        col.image(posters[i])

##########################################################################

# def fetch_poster(movie_id):
#     response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=0f0f0acdbf17f1adaa37e96010a7ee67&language=en-US".format(movie_id))
#     data = response.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/original/" + data['poster_path']


# def recommend(movie):

#     movie_index = movies[movies['title']==movie].index[0]

#     movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

#     recommended_movies = []
#     recommended_movies_poster = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].id

#         recommended_movies.append(movies.iloc[i[0]]['title'])

#         # fetch poster from API
#         recommended_movies_poster.append(fetch_poster(movie_id))

#     return recommended_movies,recommended_movies_poster

# st.title('Movie Reccomender System')

# movies = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies)

# movies_drop = movies['title'].values

# selected_movie = st.selectbox(
#     'Choose a movie!',
#     (movies_drop))

# similarity = pickle.load(open('similarity.pkl','rb'))

# if st.button('Reccomend'):
#     names,posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)


#     with col1:
#         st.text(names[0])
#         st.image(posters[0])

#     with col2:
#         st.text(names[1])
#         st.image(posters[1])

#     with col3:
#         st.text(names[2])
#         st.image(posters[2])

#     with col4:
#         st.text(names[3])
#         st.image(posters[3])

#     with col5:
#         st.text(names[4])
#         st.image(posters[4])