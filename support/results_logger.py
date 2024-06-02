"""
Logger.
"""

import datetime
import os
from config import BASE_DIR

DIR = BASE_DIR + "./_results"

METHOD_LOG_FILE_PATH = DIR + "/results.log"
TOOL_LOG_FILE_PATH = DIR + "/tool_results.log"
READABILITY_LOG_FILE_PATH = DIR + "/readability_results.log"
COGNITIVE_LOG_FILE_PATH = DIR + "/cognitive_results.log"
LOG_FILE_PATH = DIR + "/results.log"


def setup_logger():
    _create_directory_if_not_exists(DIR)
    with open(METHOD_LOG_FILE_PATH, 'w') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] Logger setup\n")

    with open(TOOL_LOG_FILE_PATH, 'w') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] Logger setup\n")

    with open(READABILITY_LOG_FILE_PATH, 'w') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] Logger setup\n")

    with open(COGNITIVE_LOG_FILE_PATH, 'w') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] Logger setup\n")


def save_result(message):
    with open(METHOD_LOG_FILE_PATH, 'a') as file:
        file.write(str(message) + '\n')


def save_tool_result(message):
    with open(TOOL_LOG_FILE_PATH, 'a') as file:
        file.write(message + '\n')


def save_readability_result(message):
    with open(READABILITY_LOG_FILE_PATH, 'a') as file:
        file.write(str(message) + '\n')


def save_cognitive_result(message):
    with open(COGNITIVE_LOG_FILE_PATH, 'a') as file:
        file.write(str(message) + '\n')


def _create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
