from fetch_reddit import get_reddit_client, search_posts
from save_data import save_to_csv

client = get_reddit_client()
posts = search_posts(client, "technostress", limit=200)
save_to_csv(posts)