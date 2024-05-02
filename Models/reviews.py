from app import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    written_review = db.Column(db.Text)
    compensation_rating = db.Column(db.Integer)
    diversity_rating = db.Column(db.Integer)
    team_rating = db.Column(db.Integer)
    management_rating = db.Column(db.Integer)
    work_life_balance_rating = db.Column(db.Integer)
    growth_rating = db.Column(db.Integer)
    feedback_review = db.Column(db.Text)
