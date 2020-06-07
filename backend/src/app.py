from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import json
import re
from random import seed
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
from articles import articles, dailyNew
from flask_cors import CORS

# init app
app = Flask(__name__)


app.secret_key = 'myawesomesecretkey'
# database connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/scrapingweb'
mongo = PyMongo(app)
CORS(app)


# add user endpoint
@app.route('/api/v1/create-user', methods=['POST'])
def create_user():
    # Receiving Data
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if username and email and password:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert(
            {'username': username, 'email': email, 'password': hashed_password})
        response = jsonify({
            '_id': str(id),
            'username': username,
            'password': hashed_password,
            'email': email
        })
        response.status_code = 201
        return response
    else:
        return not_found()


# get all user endpoint
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")


# get all news endpoint
@app.route('/api/v1/news', methods=['GET'])
def get_news():
    news = mongo.db.news.find()
    response = json_util.dumps(news)
    return Response(response, mimetype="application/json")


# filter articels by content in description
@app.route('/api/v1/filter', methods=['POST'])
def get_newsbyfilter():
    search_this_string = request.json['filter']
    print(search_this_string)
    mongo.db.news.create_index(
        [('description', 'text'), ('title', 'text'), ('author', 'text')])
    news = mongo.db.news.find(
        {'$text': {'$search': search_this_string}}).limit(5)
    print(type(news))
    response = json_util.dumps(news)
    return Response(response, mimetype="application/json")


# save articles in database endpoint
@ app.route('/api/v1/save-articles', methods=['GET'])
def get_list_articles():
    result = articles()
    if len(result) >= 1:
        # save each article in database
        mongo.db.news.insert_many(result)
        response = json_util.dumps(result)
        return Response(response, mimetype="application/json")
    else:
        return not_found()

        # save articles in database endpoint


@ app.route('/api/v1/daily-new', methods=['GET'])
def get_dailyNew():
    agr = [{'$sample': {'size': 1}}]
    # seed(1)
    # n = randint(0, 10)
    # author = mongo.db.news.find().skip(n).limit(1)
    author = mongo.db.news.aggregate(agr)
    response = json_util.dumps(author)
    return Response(response, mimetype="application/json")

# get new by id endpoint


@ app.route('/api/v1/new/<id>', methods=['GET'])
def get_new(id):
    print(id)
    new = mongo.db.news.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(new)
    return Response(response, mimetype="application/json")


# get user by id endpoint
@ app.route('/api/v1/best-author', methods=['GET'])
def get_author():
    agr = [{'$sample': {'size': 1}}]
    # seed(1)
    # n = randint(0, 10)
    # author = mongo.db.news.find().skip(n).limit(1)
    author = mongo.db.news.aggregate(agr)
    response = json_util.dumps(author)
    return Response(response, mimetype="application/json")


# get user by id endpoint
@ app.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
    print(id)
    user = mongo.db.users.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


# get user by id endpoint
@ app.route('/api/v1/add-subs', methods=['POST'])
def add_subscriber():
    email = request.json['email']
    response = json_util.dumps(email)
    if email:
        mongo.db.subscribers.insert_one({"emailSubs": email})
    else:
        response = "user email not found"
    return Response(response, mimetype="application/json")


# delete a user by id endpoint
@ app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response


# @app.route('/users/<_id>', methods=['PUT'])
# def update_user(_id):
#     username = request.json['username']
#     email = request.json['email']
#     password = request.json['password']
#     if username and email and password and _id:
#         hashed_password = generate_password_hash(password)
#         mongo.db.users.update_one(
#             {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'username': username, 'email': email, 'password': hashed_password}})
#         response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
#         response.status_code = 200
#         return response
#     else:
#         return not_found()


@ app.errorhandler(500)
def not_found(error=None):
    message = {
        'message': 'An error has occurred' + request.url,
        'status': 500
    }
    response = jsonify(message)
    response.status_code = 500
    return response


if __name__ == "__main__":
    app.run(debug=True)
