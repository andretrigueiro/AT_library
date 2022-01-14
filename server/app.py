"""

Main script that run the env - and back end? .

"""

#imports
from flask import Flask, jsonify
from flask_cors import CORS
from database.db import BOOKS

# configuration
DEBUG = True

# ----------------------------------------------------------------------------------------

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# ----------------------------------------------------------------------------------------

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# ----------------------------------------------------------------------------------------

# route handler of books
@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })

# ----------------------------------------------------------------------------------------

# main aplication
if __name__ == '__main__':
    app.run()
