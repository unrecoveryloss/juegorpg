import pymysql

def get_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",  
        db="juegorpg",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
    return connection
