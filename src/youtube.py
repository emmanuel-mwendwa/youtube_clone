from app import create_app
import os

app = create_app(os.getenv('YOUTUBE_CONFIG') or 'default')