import os
from flask import Flask, render_template, flash, request, url_for, redirect
from critters import critter_list
from feeds import BuildPod, BuildNews
from audiofiles import make_audio
import logging

PODLIST = BuildPod()

NEWSLIST = BuildNews()

CRITTERLIST = critter_list()

AUDIOFILES = make_audio()

app = Flask(__name__)


@app.route('/')
def homepage():
    postit = 'imgs/postitOBDM.png'
    return render_template('home.html', PODLIST = PODLIST, NEWSLIST = NEWSLIST, postit = postit)

@app.route('/news/')
def news():
    postit = 'imgs/postitClear.png'
    return render_template('news.html', NEWSLIST = NEWSLIST, postit = postit)

@app.route('/podcast/')
def podcast():
    postit = 'imgs/postitClear.png'
    return render_template('podcast.html', PODLIST = PODLIST, postit = postit)

@app.route('/about/')
def about():
    postit = 'imgs/postitClear.png'
    return render_template('about.html', postit = postit)

@app.route('/rundown/')
def rundown():
    return render_template('rundown.html')

@app.route('/paul/')
def paul():
    postit = 'imgs/postitClear.png'
    return render_template('paul.html', CRITTERLIST = CRITTERLIST, postit = postit)

@app.route('/media/')
def media():
    postit = 'imgs/postitClear.png'
    return render_template('media.html', postit = postit, AUDIOFILES = AUDIOFILES)

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html')
'''
@app.route('/login/', methods=["GET", "POST"])
def login_page():
    error = None
    try:
        if request.method == "POST":
            attempt_username = request.form['username']
            attempt_password = request.form['password']

            # print(attempt_username)
            # print(attempt_password)

            if attempt_username == "admin" and attempt_password == "password":
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid Login. Try again asshole"
                # print(error)
        return render_template("login.html", error = error)

    except Exception as e:
        print("printing e: ", e)
        return render_template('login.html', error = error)
'''


if __name__ == '__main__':
    app.run()
