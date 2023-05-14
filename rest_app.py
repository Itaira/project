####################
# BACKEND REST APP #
####################

from flask import Flask, request, render_template
import db_connector

app = Flask(__name__)



# Frontend
@app.route('/users/')
def index():
    return render_template('index.html')


@app.route('/users/', methods=['POST'])
def login():
    index = request.form['index']
    username = request.form['username']
    return f'You entered username: {username}, index: {index}'


# Supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    # function that creates username in DB based on received ID passed in the URL -> create user in ID=x to be {
    # “user_name”: “john”}
    if request.method == 'POST':
        request_data = request.json  # Getting the json data payload from request
        user_name = request_data.get('user_name')  # Treating request_data as a dictionary to get a value from key
        exit_code = db_connector.add_user(user_id, user_name)
        return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, exit_code  # status code

    # Returns the user name stored in the database for a given user id
    elif request.method == 'GET':
        user_name = db_connector.get_user(user_id)
        return {'user id': user_id, 'user name': user_name, 'status': 'retrieved'}, 200  # status code

    # Modify existing user name in the DB based on given json payload -> new user in ID=x will be {“user_name”:
    # “george”}
    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        db_connector.update_user(user_id, user_name)
        return {'user id': user_id, 'updated user name': user_name, 'status': 'modified'}, 200  # status code

    # Delete existing user from DB -> deletes user in ID=x
    elif request.method == 'DELETE':
        if db_connector.get_user(user_id) is None:
            return {'user_id': user_id, 'status': 'doesnt exist'}, 500
        exit_code = db_connector.delete_user(user_id)
        return {'user id': user_id, 'status': 'deleted'}, exit_code  # status code


# Create table
@app.route('/create/<obj>', methods=['GET'])
def create(obj):
    # function that creates username in DB based on received ID passed in the URL -> create user in ID=x to be {
    # “user_name”: “john”}
    if request.method == 'GET':
        if obj == 'table':
            return db_connector.create_table()
        else:
            return  500


app.run(host='127.0.0.1', debug=True, port=5000)
