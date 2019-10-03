import os

# EDIT
USERNAME = 'YOUR USER NAME OR EMAIL'
PASSWORD = 'YOUR LINKEDIN PASSWORD'
COURSES = ['PAST COURSE SLUG NAME HERE']

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), "downloads")
USE_PROXY = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None
