import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("FRONT_DEBUG")
    SECRET_KEY = os.getenv("FRONT_SECRET_KEY")
    BACK_URL = os.getenv("BACK_URL")