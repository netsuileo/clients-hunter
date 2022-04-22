from os import environ
from urllib.parse import urlencode

REDIS_HOST = environ.get("REDIS_HOST") or "localhost"
REDIS_PORT = int(environ.get("REDIS_PORT") or 6379)
REDIS_CHANNEL = environ.get("REDIS_CHANNEL") or "RAW_JOBS"

KEYWORDS = [
    "Главный бухгалтер",
    "Бухгалтер",
    "Юрист",
    "Юрисконсульт",
    "специалист по закупкам",
    "специалист по тендерам",
    "специалист по сертификации",
]

QUERY_ARGUMENTS = [
    ("area", "2"),
    ("area", "145"),
    ("clusters", "true"),
    ("employment", "full"),
    ("enable_snippets", "true"),
    ("items_on_page", "20"),
    ("label", "not_from_agency"),
    ("no_magic", "true"),
    ("order_by", "publication_time"),
    ("ored_clusters", "true"),
    ("schedule", "fullDay"),
    ("page", "0"),
    ("search_period", "1"),
    ("hhtmFrom", "vacancy_search_list"),
    ("search_field", "name"),
]

URLS = [
    "https://spb.hh.ru/search/vacancy?"
    + urlencode(QUERY_ARGUMENTS + [("text", keyword)])
    for keyword in KEYWORDS
]

JOB_LINK_SELECTOR = ".resume-search-item__name a.bloko-link"
