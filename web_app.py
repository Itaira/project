##########################
# FRONTEND WEB_INTERFACE #
##########################

from flask import Flask, request, render_template, redirect, url_for
import db_connector

app = Flask(__name__)


# Frontend
@app.route('/users/get_user_data/')
def index():
    return render_template('index.html')


@app.route('/users/get_user_data/', methods=['POST'])
def login():
    user_id = request.form['index']
    # perform search based on index
    return redirect(url_for('user', user_id=user_id))


# supported methods
@app.route('/users/get_user_data/<user_id>', methods=['GET'])
def user(user_id):
    return {'user_id': user_id, 'user_name': db_connector.get_user(user_id)}, 200  # status code


app.run(host='127.0.0.1', debug=True, port=5001)
