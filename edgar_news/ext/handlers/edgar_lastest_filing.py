from flask import jsonify
from edgar_news.ext.tasks.tasks import poll_latest_filing_feed
from edgar_news.ext.handlers.langchain_handler.summarize import get_summarization
import feedparser
import requests
from bs4 import BeautifulSoup
import re

BASE_URL = "https://www.sec.gov/"
LATEST_FILING_URL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=&company=&dateb=&owner=include&start=0&output=atom"


def get_lastest_filings_feed():
    feedparser.USER_AGENT = "Edgar_news/0.1 butokay@hotmail.com"
    feed = feedparser.parse(LATEST_FILING_URL)
    return feed


def get_first_post():
    # get the latest feed
    feed = get_lastest_filings_feed()

    # just find the first entry
    first_entry = feed.entries[0]

    user_agent = "google tttq912@hotmail.com"
    headers = {"User-Agent": user_agent}

    # send a GET request to the URL and retrieve the page content
    response = requests.get(first_entry.link, headers=headers)

    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # find all the <a> tags (links) in the HTML content
    links = soup.find_all("a")

    # filter the links to include only text files and only get the link
    text_links = [
        link.get("href") for link in links if re.search("\.txt$", link.get("href"))
    ]

    text_response = requests.get(BASE_URL + text_links[0], headers=headers)

    return text_response.content


def get_first_post_summarize() -> str:
    return get_summarization(get_first_post())
