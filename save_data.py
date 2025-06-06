import pandas as pd

def clean_and_filter(submissions):
    filtered = []
    for post in submissions:
        title = post.title.lower()
        selftext = post.selftext.lower()

        # Filtering conditions
        if (
            "study" in title or "interview" in title or
            "study" in selftext or "interview" in selftext or
            "survey" in title or "academic" in title or
            "survey" in selftext or "academic" in selftext or
            len(post.selftext.strip()) < 150
        ):
            continue  # skip this post

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