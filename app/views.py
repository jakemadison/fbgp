from flask import Flask, render_template

from app import app
from config import config

@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html', app_id=config['FB_APP_ID'])


if __name__ == '__main__':
    app.run()
