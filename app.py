from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
from models.company import Company
from models.review import Review


app = Flask(__name__)

#configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/company_ratings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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

# this is the app.py, just keeps all of the routes in one place
# routes are links on a webpage aka /about /home

@app.route('/')
def index():
    return 'Welcome to Company Rating App!'



@app.route('/companies/<int:company_id>', methods=['GET'])
def get_company(company_id):
    # Query the database for the company with the specified ID
    company = Company.query.get(company_id)

    if company is None:
        return jsonify({'error': 'Company not found'}), 404

    # Serialize the company object to JSON and return it
    return jsonify({
        'name': company.name,
    })

@app.route('/companies/<int:company_id>/reviews')
def company_reviews(company_id):
    # Query the database for reviews of the company with the specified ID
    reviews = Review.query.filter_by(company_id=company_id).all()

    if not reviews:
        return jsonify({'error': 'Reviews not found'}), 404

    # Serialize the review objects to JSON and return them
    serialized_reviews = []
    for review in reviews:
        serialized_reviews.append({
            'id': review.id,
            'compensation_rating': review.compensation_rating,
            'diversity_rating': review.diversity_rating,
            'team_rating': review.team_rating,
            'management_rating': review.management_rating,
            'work_life_balance_rating': review.work_life_balance_rating,
            'growth_rating': review.growth_rating,
            'written_review': review.written_review
        })

    return jsonify(serialized_reviews)


if __name__ == '__main__':
    app.run(debug=True)