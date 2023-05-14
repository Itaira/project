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
        print(res.json())

# Testing creating user
def create_user_testing():
    user_name, user_id= enter_input()
    res = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": user_name})
    if res.ok:
        print(res.json())
    return user_name, user_id

# Testing getting user
def get_user_testing(user_index):
    res = requests.get(f'http://127.0.0.1:5000/users/{user_index}')
    if res.ok:
        print(res.json())
    return "Equal or not", res

# Testing deleting user
def delete_user_testing(user_id):
    res = requests.delete(f'http://127.0.0.1:5000/users/{user_id}')
    if res.ok:
        print(res.json())
    return "Equal or not", res

# Testing updating user
def update_user_testing():
    user_name, user_id= enter_input()
    try:
        res = requests.put(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name": user_name})
        print(f"Updated user_name to {user_name}")
        print(res.json())
    except Exception as e:
        "Failed updating username"


# create_user_testing()
# update_user_testing()
# delete_user_testing(1)


# index_user = input("Please enter index to user")
# print("Get user:", get_user_testing(index_user))
