# config.py - Project Configuration Settings

import os

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "database", "attendance.db")
DATA_DIR = os.path.join(BASE_DIR, "data")
ENROLLED_DIR = os.path.join(DATA_DIR, "enrolled_students")
UNKNOWN_DIR = os.path.join(DATA_DIR, "unknown_faces")
LOGS_DIR = os.path.join(DATA_DIR, "attendance_logs")

# Face recognition settings
FACE_ENCODING_DIM = 128          # face_recognition library uses 128-d embeddings
RECOGNITION_THRESHOLD = 0.6      # Euclidean distance threshold (tune in Week 2)
NUM_REGISTRATION_SAMPLES = 10    # W1-T7: Capture 10 frames per student

# Camera settings
CAMERA_INDEX = 0                 # Default webcam
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Ensure directories exist
for directory in [ENROLLED_DIR, UNKNOWN_DIR, LOGS_DIR]:
    os.makedirs(directory, exist_ok=True)