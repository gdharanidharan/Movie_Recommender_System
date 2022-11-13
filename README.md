# Movies Recommender System
    Recommender systems are one of the most successful and widespread application of machine learning technologies in business. 
    
# Heroku App
    Applink : https://mov-rec-syst.herokuapp.com/

# Problem Statement

    Identify movies that customers want to watch, as demonstrated by their post - viewing rating
    Identify a list of movie recommendations, which contains at least one that theuser 
      will start watching as their next selection

# Dataset : Movielens
    https://grouplens.org/datasets/movielens/100k


# Repository Structure

    MOVIE RECOMMENDATION SYSTEM.ipynb: The Jupyter notebook containing code for the recommendation engines

    Data should be put in data folder

# Files contained in the project
    movie_recommendation_system.ipynb : python notebook code file
    movies.csv : movies data from MovieLens dataset
    ratings.csv : rating given by user to movie from MovieLens dataset

# Types of recommendation engines

    Simple Recommender:        Simple recommenders offer generalized recommendations to every user, based on movie 
                               popularity and/or genre. The basic idea behind this system is that movies that are 
                               more popular and critically acclaimed will have a higher probability of being liked
                               by the average audience. An example could be IMDB Top 250

    Content Based Recommender: Content-based recommenders: suggest similar items based on a particular item. 
                               This system uses item metadata, such as genre, director, description, actors, etc. 
                               for movies, to make these recommendations. The general idea behind these recommender 
                               systems is that if a person likes a particular item, he or she will also like an item 
                               that is similar to it. And to recommend that, it will make use of the user's past item
                               metadata. A good example could be YouTube, where based on your history, it suggests you
                               new videos that you could potentially watch

    Collaborative Filtering:   These systems are widely used, and they try to predict the rating or preference that a 
                               user would give an item-based on past ratings and preferences of other users. 
                               Collaborative filters do not require item metadata like its content-based counterparts


# Approach

    The problem was divided into several steps:

    Data Collection :  Data was collected from the MovieLens website

    EDA :              Data visualisation and summary statistics were used to extract insights 
                       and pattern from the various datasets

    Engine:            Recommending movies considering the post review ratings of users so I'm considering 
                       "Collaborative Filtering" technique for this problem statement
                       
    GUI :              Flask App
    
    Cloud :            Heroku

# Python libraries
    1. Pandas
    2. Matplotlib and seaborn
    3. scikit-learn
    4. scipy
