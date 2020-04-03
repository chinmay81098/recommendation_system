import pandas as pd
import numpy as np


def recommendation(user):
    data = pd.read_csv("./data/out.csv")
    genreTable = pd.read_csv("./data/genreTable.csv")
    movies_df = data[["movieId","title","genres","year"]]
    print(user)
    inputmovies = pd.DataFrame(user)
    userMovies = data[data["title"].isin(inputmovies["title"].tolist())]
    userMovies.drop(["genres","year"],axis=1,inplace=True)
    userMovies = userMovies.reset_index(drop=True)
    userGenre = userMovies.drop(["movieId","title"],axis=1)
    userScore = userGenre.transpose().dot(inputmovies["rating"])
    genreTable.set_index(genreTable["movieId"],inplace=True)
    genreTable.drop(["movieId"],axis=1,inplace=True)
    recommendation_df = ((genreTable*userScore).sum(axis=1))/(userScore.sum())
    recommendation_df = recommendation_df.sort_values(ascending=False)
    result = movies_df[movies_df["movieId"].isin(recommendation_df.head(20).keys())]
    result.drop(["movieId","genres"],axis=1,inplace=True)
    payload=result.to_json(orient="records")
    return payload