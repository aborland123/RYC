import requests
from app import db  # Import the database instance from app.py
from models.company import Company  # Import the Company model from models/company.py


def fetch_and_add_company_names():
    # Make a GET request to the external API to retrieve company names
    api_url = 'https://api.thecompaniesapi.com/v1/companies'
    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse the JSON response to extract company names
        company_data = response.json()
        company_names = [company['name'] for company in company_data]

        # Add the retrieved company names to the database
        for name in company_names:
            # Check if the company already exists in the database
            existing_company = Company.query.filter_by(name=name).first()
            if existing_company is None:
                # If the company does not exist, create a new entry in the database
                new_company = Company(name=name)
                db.session.add(new_company)
        
        # Commit changes to the database
        db.session.commit()
    else:
        # Handle the case when the API request fails
        print('Failed to fetch company names from the API')

# Call the function to fetch and add company names to the database
fetch_and_add_company_names()