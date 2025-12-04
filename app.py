from flask import Flask, request, url_for, session, flash, redirect
from models.Book import Book
import csv
import os


def get_html(content, title="Library"):
    return f'''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
        </head>
        <body>
            {content}
        </body>
        </html>
    '''


def initialize_csv():
    if not os.path.exists("csv/books.csv"):
        with open('csv/books.csv', 'w', encoding='utf-8', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "author", "publisher", "totalpages", "readedpages"])
            writer.writerow(["1", "1984", "George Orwell", "433", "233"])


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def inital_page():
    c = f""
    return get_html(c)

if __name__ == "__main__":
    initialize_csv()
    print("http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
