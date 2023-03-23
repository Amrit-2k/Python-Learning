from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




# create listed books

#dfjad

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.title} by {self.author}'


def add():

    new_book = Book(
        title=request.form['title'],
        author=request.form['author'],
        rating=request.form['rating']
    )
    db.session.add(new_book)
    db.session.commit()

    return render_template("add.html")

@app.route('/')
def home():
    return render_template("index.html", books=Book.query.all())
if __name__ == "__main__":
    app.run(debug=True)

