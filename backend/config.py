import os
from dotenv import load_dotenv
load_dotenv()

# Get the environment variable to check production mode
PROFILES = os.getenv("PROFILES", "dev")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS")
DB_URL = os.getenv("DB_URL")
