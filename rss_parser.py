
import feedparser
from datetime import datetime, timedelta, timezone
from dateutil import parser

def read_feed_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls

def get_jobs_posted_last_5_minutes(entries):
    """Filter jobs to include only those posted in the last 5 minutes."""
    now = datetime.now(timezone.utc)  # Make 'now' offset-aware by specifying UTC timezone
    five_minutes_ago = now - timedelta(minutes=300)
    recent_jobs = []
    for job in entries:
        # Parse the published date
        published_date = parser.parse(job.published)
        # Ensure comparison is between same types of datetime objects
        if published_date.tzinfo is None:
            published_date = published_date.replace(tzinfo=timezone.utc)
        if published_date > five_minutes_ago:
            recent_jobs.append(job)
    return recent_jobs

def get_latest_jobs_from_all_feeds(file_path):
    all_jobs = []
    urls = read_feed_urls(file_path)
    for url in urls:
        feed = feedparser.parse(url)
        recent_jobs = get_jobs_posted_last_5_minutes(feed.entries)
        all_jobs.extend(recent_jobs)
    return all_jobs

if __name__ == "__main__":
    file_path = 'feed_urls.txt'
    all_jobs = get_latest_jobs_from_all_feeds(file_path)
    print(f"Found {len(all_jobs)} recent jobs.")
    for job in all_jobs:
        print(job.title, job.published)  # Example of printing job titles and published dates

