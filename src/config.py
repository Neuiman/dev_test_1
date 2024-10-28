from dotenv.main import load_dotenv

import os

load_dotenv()

class settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    URL_FOR_REVISION = os.getenv("URL_FOR_REVISION")

