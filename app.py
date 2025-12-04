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