import os
import logging
from datetime import datetime

# Project root folder path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# __file__ = us_visa/logger/__init__.py
# 1 level  = us_visa
# 2 level  = US-VISA-ML (project root)

# Logs folder path project root ke andar
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOG_DIR, exist_ok=True)  # folder create if not exist

# Log file ka naam
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Logging setup
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
)
