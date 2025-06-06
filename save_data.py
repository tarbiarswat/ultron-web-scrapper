import pandas as pd
from langdetect import detect

def clean_and_filter(submissions):
    filtered = []
    for post in submissions:
        title = post.title.lower()
        selftext = post.selftext.lower()

        # Filter conditions
        if (
            "study" in title or "interview" in title or
            "study" in selftext or "interview" in selftext or
            len(selftext.strip()) < 150 or
            post.score < 5 or
            post.num_comments < 3
        ):
            continue

        # Language detection
        try:
            if detect(selftext) != "en":
                continue
        except:
            continue

        filtered.append(post)

    return filtered

def save_to_csv(submissions, filename="technostress_posts.csv"):
    filtered_submissions = clean_and_filter(submissions)

    data = [{
        "title": post.title,
        "selftext": post.selftext,
        "author": str(post.author),
        "score": post.score,
        "url": post.url,
        "created_utc": post.created_utc,
        "num_comments": post.num_comments,
        "subreddit": str(post.subreddit),
    } for post in filtered_submissions]

    pd.DataFrame(data).to_csv(filename, index=False)
    print(f"✅ Saved {len(filtered_submissions)} posts to {filename}")
