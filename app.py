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
        os.makedirs("csv", exist_ok=True)
        with open('csv/books.csv', 'w', encoding='utf-8', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "author", "publisher", "totalpages", "readedpages"])
            writer.writerow(["1", "1984", "George Orwell", "433", "233"])


def read_csv():
    Books = []
    try:
        with open('csv/books.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                book = Book()
                book.setId(r['id'])
                book.setName(r['name'])
                book.setAuthor(r['author'])
                book.setPublisher(r['publisher'])
                book.setTotalPages(r['totalpages'])
                book.setReadedPages(r['readedpages'])
                Books.append(book)
    except FileNotFoundError:
        print("Didn't find the file")
    except Exception as e:
        print(f"Error: \n {e}")
    finally:
        return Books


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def inital_page():
    l = read_csv()
    c = f"{l[0].getName()}"
    return get_html(c)


if __name__ == "__main__":
    initialize_csv()
    print("http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
