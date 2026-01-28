import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("BACK_DEBUG")
    SECRET_KEY = os.getenv("BACK_SECRET_KEY")
    MONGO_URI = os.getenv("MONGO_URI")