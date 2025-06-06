import praw
from config import REDDIT_CONFIG

def get_reddit_client():
    return praw.Reddit(**REDDIT_CONFIG)

def search_posts(client, keyword, limit=100):
    return client.subreddit("all").search(keyword, limit=limit)
