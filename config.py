import os
from dotenv import load_dotenv
load_dotenv()

# Get the environment variable to check production mode
PRODUCTION = os.getenv("PRODUCTION", "dev")
PRODUCTION_DB_URL = os.getenv("PRODUCTION_DB_URL")
