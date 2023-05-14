import datetime
import pymysql


################################
# DATABASE_CONNECTOR FUNCTIONS #
################################


# Establishing connection to DB
def establish_connection():
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql7.freemysqlhosting.net', port=3306, user='sql7618046', passwd='5gmv8QFsi8',
                           db='sql7618046')  # Bad practice
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    return cursor, conn


# Close connection to DB
def close_connection(conn, cursor):
    cursor.close()
    conn.close()
    return "Connection closed", 200


def create_table():
    # Getting a cursor from Database
    cursor, conn = establish_connection()

    statementToExecute = "CREATE TABLE users (id INT NOT NULL, name VARCHAR(45) NOT NULL, creation_date VARCHAR(45) NOT NULL, PRIMARY KEY (id));"
    try:
        cursor.execute(statementToExecute)
        close_connection(conn, cursor)
        return {"result": "Table users created successfully"} , 200
    except Exception as e:
        close_connection(conn, cursor)
        return "Table users already exists", 200


# Add user to DB
def add_user(user_id, user_name):
    # Getting a cursor from Database
    cursor, conn = establish_connection()

    try:
        # Inserting data into table
        cursor.execute(
            f"INSERT INTO users (name,id,creation_date) VALUES ('{user_name}',{user_id},'{str(datetime.datetime.now())}')")
        # Close connection
        close_connection(conn, cursor)
        print("Created successfully")
        return 200
    except Exception as e:
        print("Creation failed")
        return 500


# Get row based on user id given
def get_user(user_id):
    # Getting a cursor from Database
    cursor, conn = establish_connection()

    cursor.execute(f"SELECT name FROM users WHERE id={user_id}")
    user_name = cursor.fetchone()
    close_connection(conn, cursor)
    if user_name:
        return user_name
    return None


# Delete row based on user id given
def delete_user(user_id):
    # Getting a cursor from Database
    cursor, conn = establish_connection()
    cursor.execute(f"DELETE FROM users WHERE id={user_id}")
    close_connection(conn, cursor)
    return 200


# Update values in ID number to new username
def update_user(user_id, user_name):
    # Getting a cursor from Database
    cursor, conn = establish_connection()
    try:
        cursor.execute(f"UPDATE users SET name='{user_name}' WHERE id={user_id}")
        close_connection(conn, cursor)
        return 200
    except Exception as e:
        close_connection(conn, cursor)
        return 500


