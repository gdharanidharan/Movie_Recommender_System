from flask import Flask,render_template,request
import flask
import pickle
import numpy as np
import pandas as pd

ratings_matrix_users = pickle.load(open('ratings_matrix_users.pkl','rb'))
df_similar_user = pickle.load(open('df_similar_user.pkl','rb'))
df_movies = pickle.load(open('df_movies.pkl','rb'))
df_ratings = pickle.load(open('df_ratings.pkl','rb'))
df_movies_ratings = pickle.load(open('df_movies_ratings.pkl','rb'))

app = Flask(__name__)


def getRecommendedMoviesAsperUserSimilarity(userId):
    """
     Recommending movies which user hasn't watched as per User Similarity
    :param user_id: user_id to whom movie needs to be recommended
    :return: movieIds to user 
    """
    user2Movies= df_ratings[df_ratings['userId']== userId]['movieId']
    sim_user=df_similar_user.loc[userId].values[0]
    df_recommended=pd.DataFrame(columns=['movieId','title','genres','userId','rating','timestamp'])
    for movieId in df_ratings[df_ratings['userId']== sim_user]['movieId']:
        if movieId not in user2Movies:
            df_new= df_movies_ratings[(df_movies_ratings.userId==sim_user) & (df_movies_ratings.movieId==movieId)]
            df_recommended=pd.concat([df_recommended,df_new])
    best10_df  = df_recommended.sort_values(by='rating', ascending=True)[0:10]
    return best10_df[['title']]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Predict', methods =["GET", "POST"])
def UserLogin():
    if request.method == "POST":
        userId = request.form.get('userId')
        userId = int(userId)
        recommend_movies = getRecommendedMoviesAsperUserSimilarity(userId)
        recommend_movies = recommend_movies.reset_index(drop=True)
        recommend_movies.columns = ['Movie Names']
        
        return render_template("simple.html", column_names=recommend_movies.columns.values, row_data=list(recommend_movies.values.tolist()),
                            link_column="Patient ID", zip=zip)


if __name__ == '__main__':
    app.run(debug=True)