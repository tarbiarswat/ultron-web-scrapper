from fetch_reddit import get_reddit_client, search_posts
from save_data import save_to_csv

client = get_reddit_client()

keywords = [
    "technostress", "tech fatigue", "digital burnout",
    "technology stress", "screen anxiety", "remote work stress"
]

all_posts = []

print("🔍 Searching Reddit for keywords related to technostress...")

for kw in keywords:
    print(f"→ Searching: {kw}")
    results = search_posts(client, kw, limit=200)
    all_posts.extend(results)

print(f"🔎 {len(all_posts)} total posts fetched. Now filtering...")

save_to_csv(all_posts)