from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Settings:
    MONGO_URI = os.getenv("MONGO_URI")  # Fetch the MongoDB URI from the .env file

settings = Settings()