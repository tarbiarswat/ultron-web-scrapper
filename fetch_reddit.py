import praw
from config import REDDIT_CONFIG

def get_reddit_client():
    return praw.Reddit(**REDDIT_CONFIG)

def search_posts(client, keyword, limit=200):
    return client.subreddit("all").search(keyword, limit=limit)