from flask import Flask, render_template, request, redirect,url_for
app = Flask(__name__)

books=[
    {"id":38,"title":"The Count of Monte Cristo","author":"Alexandre Dumas","year":1844},
    {"id":39,"title":"The Three Musketeers","author":"Alexandre Dumas","year":1844},
    {"id":40,"title":"The Old Man and the Sea","author":"Ernest Hemingway","year":1952},
    {"id":41,"title":"For Whom the Bell Tolls","author":"Ernest Hemingway","year":1940},
    {"id":42,"title":"A Farewell to Arms","author":"Ernest Hemingway","year":1929},
    {"id":43,"title":"Lolita","author":"Vladimir Nabokov","year":1955},
    {"id":44,"title":"Madame Bovary","author":"Gustave Flaubert","year":1857},
    {"id":45,"title":"The Stranger","author":"Albert Camus","year":1942},
    {"id":46,"title":"The Plague","author":"Albert Camus","year":1947},
    {"id":47,"title":"The Sun Also Rises","author":"Ernest Hemingway","year":1926},
    {"id":48,"title":"Heart of Darkness","author":"Joseph Conrad","year":1899},
    {"id":49,"title":"The Metamorphosis","author":"Franz Kafka","year":1915},
    {"id":50,"title":"The Trial","author":"Franz Kafka","year":1925}
]

    


@app.route('/')
def index():
    return render_template('index.html',books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        data = request.form

        new_book = {
            "id": books[-1]["id"] + 1 if books else 1,
            "title": data.get("title"),
            "author": data.get("author"),
            "year": int(data.get("year"))
        }

        books.append(new_book)
        return redirect(url_for('index'))

    return render_template('add_book.html')

@app.route('/update/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    book = None
    for b in books:
        if b["id"] == book_id:
            book = b
            break

    if not book:
        return "Book not found", 404

    if request.method == 'POST':
        data = request.form
        book.update({
            "title": data.get("title", book["title"]),
            "author": data.get("author", book["author"]),
            "year": int(data.get("year", book["year"])),
        })
        return redirect(url_for('index'))

    return render_template('update_book.html', book=book)

@app.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return redirect(url_for('index'))


if __name__=="__main__":
    app.run()