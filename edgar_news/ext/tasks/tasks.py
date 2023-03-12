import feedparser
from celery import Celery

app = Celery("tasks", backend="rpc://", broker="redis://localhost:6379/0")
URL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=&company=&dateb=&owner=include&start=0&output=atom"


@app.task
def poll_latest_filing_feed(url) -> None:
    feedparser.USER_AGENT = "Edgar_news/0.1 butokay@hotmail.com"
    feed = feedparser.parse(url)
    return feed


app.conf.beat_schedule = {
    "poll_feed": {
        "task": "tasks.poll_latest_filing_feed",
        "schedule": 60.0,  # Run the task every 60 seconds
        "args": (URL),  # Replace with the URL of the RSS feed you want to track
    },
}
