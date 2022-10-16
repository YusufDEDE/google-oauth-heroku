"""Flask configuration variables."""
from os import path, getenv
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    # General Config
    SECRET_KEY = getenv("SECRET_KEY")
    HOST = getenv('HOST', '127.0.0.1')
    PORT = getenv('PORT', 5000)
    DEBUG = True if getenv('DEBUG') == 'True' else False

    CLIENT_ID: str = getenv("CLIENT_ID")
    PROJECT_ID: str = getenv("PROJECT_ID")
    AUTH_URI: str = getenv("AUTH_URI")
    TOKEN_URI: str = getenv("TOKEN_URI")
    AUTH_PROVIDER_X509_CERT_URL: str = getenv("AUTH_PROVIDER_X509_CERT_URL")
    CLIENT_SECRET: str = getenv("CLIENT_SECRET")
    REDIRECT_URIS: str = getenv("REDIRECT_URIS")
    JAVASCRIPT_ORIGINS: str = getenv("JAVASCRIPT_ORIGINS")
