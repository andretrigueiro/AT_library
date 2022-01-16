"""

Main script that run the env - and back end? .

"""

#imports
from flask import Flask, jsonify, request
from flask_cors import CORS
from database.db import BOOKS
import json

# configuration
DEBUG = True

# ----------------------------------------------------------------------------------------

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# ----------------------------------------------------------------------------------------

# help functions

# validate the post request
def validate_post(requested):
    if 'title' not in requested:
        print("No title in given POST.")
        return False
    if 'author' not in requested:
        print("No author in given POST.")
        return False
    if 'read' not in requested:
        print("No read stats in given POST.")
        return False
    else:
        return True

# search books on database
def search_book_on_list(value):
    return next((item for item in BOOKS if item['title'] == value), None)

# ----------------------------------------------------------------------------------------

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# ----------------------------------------------------------------------------------------

# route handler of books
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        if validate_post(post_data):
            title_check = post_data.get('title')
            if search_book_on_list(title_check):
                response_object = {'status': 'error'}
                response_object['message'] = 'Book already added!'
            else:
                BOOKS.append({
                    'title': post_data.get('title'),
                    'author': post_data.get('author'),
                    'read': post_data.get('read')
                })
                response_object['message'] = 'Book added!'
        else:
            response_object = {'status': 'error'}
            response_object['message'] = 'Invalid request!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

# ----------------------------------------------------------------------------------------

# main aplication
if __name__ == '__main__':
    app.run()
