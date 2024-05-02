from flask_testing import TestCase
from app import app, db
from models.review import Review
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from unittest.mock import MagicMock
import requests_mock



class TestCompanyReviews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app
    

    def setUp(self):
        db.create_all()

        # Insert test data into the database
        review1 = Review(company_id=1, compensation_rating=5, diversity_rating=4, team_rating=3, management_rating=4, work_life_balance_rating=2, growth_rating=2, written_review="love this place", feedback_reviews="fire managers") 
        review2 = Review(company_id=1, compensation_rating=3, diversity_rating=5, team_rating=3, management_rating=4, work_life_balance_rating=2, growth_rating=2, written_review="this place sucks", feedback_reviews="hire more managers")
        db.session.add(review1)
        db.session.add(review2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_company_reviews_route(self):
        response = self.client.get('/companies/1/reviews')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIsInstance(data, list)  # Assert that the response is a list of reviews