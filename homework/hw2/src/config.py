from dotenv import load_dotenv
import os

def load_env():
    """Load environment variables from .env file."""
    load_dotenv()

def get_key(key_name):
    """Retrieve the value of a specified environment variable."""
    return os.getenv(key_name)
