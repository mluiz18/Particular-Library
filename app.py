from flask import Flask, request, url_for, session, flash, redirect
from models.Book import Book


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


b1 = Book()
b1.setName("1984")

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def inital_page():
    c = f"{b1.getName()}"
    return get_html(c)

if __name__ == "__main__":
    print("http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
