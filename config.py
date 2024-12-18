import os
from dotenv import load_dotenv
load_dotenv()

# Get the environment variable to check production mode
PRODUCTION = os.getenv("PRODUCTION", "dev")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS")
PRODUCTION_DB_URL = os.getenv("PRODUCTION_DB_URL")
