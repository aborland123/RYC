from flask import Flask, jsonify

# this is the app.py, just keeps all of the routes in one place
# routes are links on a webpage aka /about /home

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the homepage!'

# Define another route for a different page
@app.route('/about')
def about():
    return 'This is the about page.'

# Sample data for demonstration purposes
companies = [
    {"name": "Google", "location": "Mountain View, CA", "industry": "Technology"},
    {"name": "Apple", "location": "Cupertino, CA", "industry": "Technology"},
    {"name": "Microsoft", "location": "Redmond, WA", "industry": "Technology"}
]

@app.route('/api/companies')
def get_companies():
    return jsonify(companies)

if __name__ == '__main__':
    app.run(debug=True)