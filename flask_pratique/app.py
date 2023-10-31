from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)












if __name__ == '__main__':
    app.run(debug=True, port=5000)