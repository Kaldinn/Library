from flask import Flask, render_template
import services.books as Book

app = Flask(__name__)

@app.route("/")
def books():
    books = Book.get_all()[0:100]
    return render_template("index.html", books = books)

if __name__ == "__main__":
    app.run(debug=True, port=3000)

