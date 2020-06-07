from dictionary import getArticles, getArticleDaily
from newspaper import Article
import json
import nltk
import random

# function for return articles


def articles():
    articlesList = []
    # get articles of dictionary set argument of totally articles returns
    source = getArticles(15)
    nltk.download('punkt')
    # bucle for to set ten articles in the array articlesList
    for url in source:
        article = Article(url, lenguage="es")
        article.download()
        article.parse()
        article.nlp()
        articleData = {
            "title": article.title,
            "author": article.authors,
            "publish_date": article.publish_date,
            "description": article.text,
            "summary": article.summary,
            "keywords": article.keywords,
            "image": article.top_image,
            "video": article.movies
        }
        articlesList.append(articleData)
    return articlesList


def dailyNew():
    source = getArticleDaily()
    new = Article(source, lenguage="es")
    nltk.download('punkt')
    new.download()
    new.parse()
    new.nlp()
    newDaily = {
        "title": new.title,
        "author": new.authors,
        "publish_date": article.publish_date,
        "description": new.text,
        "summary": new.summary,
        "image": new.top_image,
        "video": new.movies
    }
    if len(newDaily) > 1:
        return newDaily
    else:
        return {"message": "no daily new"}
