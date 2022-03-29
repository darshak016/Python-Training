import sqlite3
from flask import Flask, Response, request
import requests
import collections
import json

app = Flask(__name__)
DATABASE = 'book_details.db'

@app.route("/get_books/",methods=["GET"])
def get_books():
    try:    
       connection = sqlite3.connect(DATABASE)
       cursor = connection.cursor()
       query = """SELECT * FROM BOOKS"""
       all_book_data = cursor.execute(query).fetchall()
       connection.close() 
       obj_list = []
       for row in all_book_data:
        d = collections.OrderedDict()
        d['id'] = row[0]
        d['BookName'] = row[1]
        d['Author'] = row[2]
        d['Cost'] = row[3]
        d['ISBN No'] = row[4]
        obj_list.append(d)       
    except Exception as e:
        return Response(f"Exception : {e}",status=500)  
    else:
        res = json.dumps(obj_list)
        return Response(res,status=200) #return

@app.route('/insert_book/',methods=['POST'])        
def insert_data():
    book_name = request.form["book_name"]
    author_name = request.form["author_name"]
    cost = request.form["cost"]
    isbn_num = request.form["isbn_num"]
    print(book_name)
    sql_query = """INSERT INTO BOOKS(BookName,Author,Cost,isbnNo) VALUES(?,?,?,?)"""
    values = (book_name, author_name, cost, isbn_num)
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, values)
        connection.commit()
        connection.close()
    except Exception as e:
        return Response(f"Exception : {e}",status=500)
    else:
        return Response("success",status=200)
        
@app.route('/delete/',methods=["DELETE"])
def delete_data():
    book_id = request.form["book_id"]
    sql_query = """DELETE FROM BOOKS WHERE BookId=?"""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, (book_id,))
        connection.commit()
    except Exception as e:
        return Response(f"Exception : {e}",status=500)
    else:
        connection.close()
        return Response("Data Deleted Successfully!",status=200)

@app.route('/update/',methods=["PUT"])
def update_table():
    book_id = request.form["book_id"]
    book_name = request.form["book_name"]
    author_name = request.form["author_name"]
    cost = request.form["cost"]
    isbn_num = request.form["isbn_num"]
    
    query = """UPDATE BOOKS SET BookName='{}',Author='{}',
    Cost='{}',isbnNo='{}' WHERE BookId='{}'""".format(book_name,author_name,cost,isbn_num,book_id)
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        return Response(f"Exception : {e}",status=500)
    else:
        connection.close()
        return Response("Table updated",status=200)
    
if __name__ == "__main__":
    query = """ CREATE TABLE IF NOT EXISTS BOOKS( BookId INTEGER PRIMARY KEY AUTOINCREMENT,
    BookName varchar(255),
    Author varchar(255),
    Cost int,
    isbnNo int)"""
    
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    print("Table Created Successfully!")
    get_books()
    app.run(port=4000, debug=True)        