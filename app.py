import json
from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


# Load the 'databases'
with open('data/books.json') as json_data:
    book_db = json.load(json_data)

with open('data/people.json') as json_data:
    user_db = json.load(json_data)


### General Routes
@app.route("/")
def hello():
    ### Links:
    links = ""
    links += "<h1>End Points:</h1>"
    links += "<ul>"
    links += "<li><a href='/'>/</a> (You are here)</li>"
    links += "<li><a href='/users'>/users</a></li>"
    links += "<li><a href='user/1'>/user/#</a> (switch out 1 for another number to see a different user)</li>"
    links += "<li><a href='/books'>/books</a></li>"
    links += "<li><a href='book/1'>/book/#</a> (switch out 1 for another number to see a different book)</li>"
    links += "</ul>"
    return links


### User Routes
@app.route("/users", methods=['GET'])
def get_users():
    return jsonify(user_db)

@app.route("/user/<int:user_id>", methods=['GET'])
def get_user(user_id):
    input_dict = user_db

    # Filter python objects with list comprehensions
    output_dict = [x for x in input_dict if x['id'] == user_id]

    return jsonify(output_dict)

@app.route("/user/add", methods=['POST'])
def new_user():
    resp = "Unable to add user"
    return jsonify(resp)


### Book Routes
@app.route("/books", methods=['GET'])
def get_books():
    resp = book_db
    return jsonify(resp)

@app.route("/book/<int:book_id>", methods=['GET'])
def get_book(book_id):
    input_dict = book_db

    # Filter python objects with list comprehensions
    output_dict = [x for x in input_dict if x['id'] == book_id]

    return jsonify(output_dict)

@app.route("/book/add", methods=['POST'])
def new_book():
    new_id = len(book_db) + 1
    data = request.json

    try:
        new_book = {
            "id": new_id,
            "author_first_name": data['author_first_name'],
            "author_last_name": data['author_last_name'],
            "title": data['title'],
            "pages": data['pages']}
        book_db.append(new_book)
    except KeyError:
        resp = "Book not added. Incorrect data format"
        return jsonify(resp)

    resp = "Book added"
    return jsonify(resp)


# The main entry point for the program
if __name__ == "__main__":
    # adding host='0.0.0.0' to the app.run() is needed if connecting using Vagrant
    app.run(host='0.0.0.0')
