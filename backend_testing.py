import time
import db_connector
import requests

# Collecting input from users
def enter_input():
    user_name = input("Enter the user name:")
    user_id = input("Enter the index to write to:")
    return user_name, user_id

# Testing creating table
def create_table_testing():
    res = requests.post(f'http://127.0.0.1:5000/create/table')
    if res.ok:
        print('SUCCESS: ', res.json())
    else:
        print('ERROR: Failed to create table')

# Testing creating user
def create_user_testing(user_name, user_id):
    res = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": user_name})
    if res.ok:
        print('SUCCESS: ',res.json())
    else:
        print('ERROR: Failed to create user')
    return user_name, user_id

# Testing getting user
def get_user_testing(user_id):
    res = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
    if res.ok:
        print('SUCCESS: ',res.json())
    else:
        print('ERROR: Failed to retrieve user')
    return "Equal or not", res

# Checking if user exists after creation directly from the DB ( Using db_connector funcs )
def check_user_db_testing(user_name, user_id):
    cursor, conn = db_connector.establish_connection()
    statementToExecute = f"SELECT * FROM users WHERE id={user_id} AND name='{user_name}';"
    cursor.execute(statementToExecute)
    result = cursor.fetchone()
    # Check if "testing_user" is stored under id 999
    if result:
        print("SUCCESS: User 'testing_user' is stored under id 999")
    else:
        print("FAIL: User 'testing_user' is not stored under id 999")
    db_connector.close_connection(conn,cursor)

# Testing deleting user
def delete_user_testing(user_id):
    res = requests.delete(f'http://127.0.0.1:5000/users/{user_id}')
    if res.ok:
        print(res.json())
    else:
        print("ERROR: Deletion failed")
    return res

# Testing updating user
def update_user_testing(user_name, user_id):
    try:
        res = requests.put(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": user_name})
        print(f"SUCCESS: Updated user_name to {user_name}")
        print(res.json())
    except Exception as e:
        "ERROR: Failed updating username"

# TESTING SEQUENCE

# # Functions with testing values
# user="testing_user"
# update_to_user="testing_update_user"
# index="999"
#
#
# create_user_testing(user,index)
# time.sleep(2)
# check_user_db_testing(user,index)
# time.sleep(2)
# update_user_testing(update_to_user,index)
# time.sleep(2)
# get_user_testing(index)
# time.sleep(2)
# delete_user_testing(index)
# time.sleep(2)
# check_user_db_testing(user,index)

