from os import environ

JOBS_SET = environ.get("JOBS_SET") or "SENT_JOBS"
RAW_JOBS_CHANNEL = environ.get("RAW_JOBS_CHANNEL") or "RAW_JOBS"
FILTERED_JOBS_CHANNEL = environ.get("FILTERED_JOBS_CHANNEL") or "FILTERED_JOBS"
REDIS_HOST = environ.get("REDIS_HOST") or "localhost"
REDIS_PORT = int(environ.get("REDIS_PORT") or 6379)
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
