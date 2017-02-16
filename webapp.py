from flask import Flask, url_for, flash, render_template, redirect, request, g, send_from_directory
from flask import session as login_session
from model import *
from werkzeug.utils import secure_filename
import locale, os


app = Flask(__name__)


@app.route('/')
def showAllMovies():
	allmovies = session.query(Movie).all()
	return render_template('main.html', allmovies = allmovies)


@app.route('/details')
def movies(movie_id):
	movies=session.query(Movie).all
	return render_template('details.html',movies=movies)

if __name__ == '__main__':
	app.run(debug=True)