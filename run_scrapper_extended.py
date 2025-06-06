from fetch_reddit import get_reddit_client, search_posts
from fetch_pushshift import fetch_pushshift
from save_data_extended import save_to_csv
from logger import setup_logger

logger = setup_logger()
client = get_reddit_client()

keywords = [
    "technostress", "tech fatigue", "digital burnout",
    "technology stress", "screen anxiety", "remote work stress"
]

all_posts = []

logger.info("🔍 Starting Reddit + Pushshift data scraping...")

# Reddit API scrape
for kw in keywords:
    logger.info(f"📦 Searching Reddit API: {kw}")
    results = search_posts(client, kw, limit=200)
    all_posts.extend(results)

# Pushshift scrape
for kw in keywords:
    logger.info(f"📦 Searching Pushshift: {kw}")
    data = fetch_pushshift(kw, size=200)
    for item in data:
        class Dummy:
            pass
        p = Dummy()
        p.title = item.get("title", "")
        p.selftext = item.get("selftext", "")
        p.score = item.get("score", 0)
        p.num_comments = item.get("num_comments", 0)
        p.created_utc = item.get("created_utc", "")
        p.url = item.get("full_link", "")
        p.subreddit = item.get("subreddit", "")
        p.author = item.get("author", "unknown")
        all_posts.append(p)

logger.info(f"🔎 Total posts fetched before filtering: {len(all_posts)}")

save_to_csv(all_posts, logger)
