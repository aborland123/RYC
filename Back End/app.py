from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/company_ratings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# this is the app.py, just keeps all of the routes in one place
# routes are links on a webpage aka /about /home



@app.route('/')
def index():
    return 'Welcome to Company Rating App!'

@app.route('/companies')
def list_companies():
    return 'List of Companies'

@app.route('/companies/<int:company_id>')
def company_details(company_id):
    return f'Details of Company with ID {company_id}'

@app.route('/companies/<int:company_id>/reviews')
def company_reviews(company_id):
    return f'Reviews of Company with ID {company_id}'

# creating a database model
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)

# creating a database model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    company = db.relationship('Company', backref=db.backref('reviews', lazy=True))

if __name__ == '__main__':
    app.run(debug=True)