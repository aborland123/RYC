from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests


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

@app.route('/api/companies', methods=['GET'])
def get_company_names():
    # Make a GET request to the external API to retrieve company names
    api_url = 'https://api.thecompaniesapi.com/v1/companies'
    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse the JSON response to extract company names
        company_data = response.json()
        company_names = [company['name'] for company in company_data]

        # Return the company names as JSON response
        return jsonify(company_names)
    else:
        # Return an error response if the API request fails
        return jsonify({'error': 'Failed to fetch company names from the API'}), response.status_code

@app.route('/companies/<int:company_id>')
def company_details(company_id):
    return f'Details of Company with ID {company_id}'

@app.route('/companies/<int:company_id>/reviews')
def company_reviews(company_id):
    return f'Reviews of Company with ID {company_id}'

from flask import jsonify

@app.route('/companies/<int:company_id>', methods=['GET'])
def get_company(company_id):
    # Logic to retrieve company details from the database based on the company_id
    # Replace this with actual logic to query the database

    # For demonstration purposes, let's assume we have a Company model defined
    # and we're using SQLAlchemy to query the database
    company = Company.query.get(company_id)

    if company is None:
        return jsonify({'error': 'Company not found'}), 404

    # Serialize the company object to JSON and return it
    return jsonify({
        'id': company.id,
        'name': company.name,
        'description': company.description
    })


if __name__ == '__main__':
    app.run(debug=True)