from flask import Flask, request, jsonify
import sqlite3
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/resources/books/all', methods=['GET'])
def get_all():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    select_books = "SELECT * FROM books"
    result = cursor.execute(select_books).fetchall()
    connection.close()
    return jsonify(result)

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.route('/api/v1/resources/books/authors', methods=['GET'])


# 2.Ruta para obtener los libros de un autor en la llamada
@app.route('/api/v1/resources/books/author', methods=['GET'])


# 3.Ruta para obtener los libros filtrados por title, publicación y autor
@app.route('/api/v1/resources/books/filters', methods=['GET'])


app.run()