import os

class Config:
    def __init__(self):
        self.VIDEO_EXTENSIONS = ('.mp4', '.mkv', '.avi', '.mov', '.flv')
        self.MAX_WORKERS = max(1, os.cpu_count() // 2)