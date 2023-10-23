# Movie_recommendation_system
Movie recommendation using jupyter notebook and Streamlit library in Python
1)This reccomendation system uses content based filtering so in the case of MOVIES so this code uses the common directors and key words from the gist to recommend movies 
2)The dataset from Kaggle(https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) download it as zip and then extract it.
3)The python code uses streamlit library for creating the interface and uses API to fetch the posters of the movies
--->you can get the api from the https://www.themoviedb.org/settings/api remember to create a account first then get the api key
--->then use API access token key from profile\settings to get the acces to your api
---->after getting the api key we have to add the poster path to fetch the posters 
4)To create the frontend refer to the streamlit docs its easier to code using streamlit
5)the pkl file named similarity.pk lc ould not be uploaded because of it's size being more than 25MB, but the file can be created by the code given in the jupyter-notebook using pickle library.
6)run the code using the following command in the terminal

$streamlit run <'name_of_your_py_file'.py>


