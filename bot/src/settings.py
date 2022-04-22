from os import environ

API_TOKEN = environ.get("API_TOKEN")
CHANNEL_NAME = environ.get("CHANNEL_NAME")
REDIS_HOST = environ.get("REDIS_HOST") or "localhost"
REDIS_PORT = int(environ.get("REDIS_PORT") or 6379)
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
REDIS_JOBS_CHANNEL = environ.get("REDIS_JOBS_CHANNEL") or "FILTERED_JOBS"
