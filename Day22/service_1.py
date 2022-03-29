import requests
from flask import Flask, redirect, url_for, request, Response
import json

app = Flask(__name__)

# URL and PORT
ENDPOINT = "http://127.0.0.1:{0}/{1}/"
PORT = "4000"

# API Methods
READBOOKS = "get_books"
DELETEBOOKS = "delete"
ADDBOOKS = "insert_book"
EDITBOOKS = "update"

# print(ENDPOINT.format(PORT, READBOOKS))


@app.route("/get_list", methods=["GET", "POST"])
def get_list():
    try:
        response = requests.get(ENDPOINT.format(PORT, READBOOKS))
    except Exception as e:
        return Response(f"Exception : {e}", status=500)
    else:
        if response.status_code == 200:
            return Response(json.dumps(response.json()), status=200)
        else:
            return Response(response.text, status=500)


@app.route("/delete_book", methods=["POST"])
def delete_books():
    try:

        data = {"book_id" : request.form["book_id"]}
        response = requests.delete(ENDPOINT.format(PORT, DELETEBOOKS), data=data)

    except Exception as e:
        return Response(f"Exception : {e}", status=500)
    else:
        if response.status_code == 200:
            return Response("Successfully Deleted", status=200)
        else:
            return Response(response.text, status=500)


@app.route("/add_book", methods=["POST"])
def add_books():

    data = request.form
    try:
        response = requests.post(ENDPOINT.format(PORT, ADDBOOKS), data=data)
        print("add books", response)
    except Exception as e:
        return Response(f"Exception : {e}", status=500)
    else:
        if response.status_code == 200:
            return "Thank You for adding book"
        else:
            return Response(response.text, status=500)


@app.route("/edit_book", methods=["POST"])
def edit_books():
    data = request.form
    try:
        response = requests.put(ENDPOINT.format(PORT, EDITBOOKS), data=data)
    except Exception as e:
        return Response(f"Exception : {e}", status=500)
    else:
        if response.status_code == 200:
            return "Successfully edited the book"
        else:
            return Response(response.text, status=500)


if __name__ == "__main__":
    app.run(debug=True)
