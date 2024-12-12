import os

class Config:
    # Use environment variables for sensitive information or default to hardcoded strings for testing
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:DevOps2024%2A%40@database-3.cdug00k6kj78.us-east-1.rds.amazonaws.com/webappdb?sslmode=require'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
