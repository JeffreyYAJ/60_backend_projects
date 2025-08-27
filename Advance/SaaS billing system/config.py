import os

class Config:
    SECRET_KEY= 'yaj'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///saas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt_yaj'
    STRIPE_API_KEY = 'stripe_yaj'
    