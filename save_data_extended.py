import pandas as pd
from langdetect import detect
from tracker import log_activity

def clean_and_filter(submissions, logger):
    filtered = []
    errors = []

    for post in submissions:
        try:
            title = post.title.lower()
            selftext = post.selftext.lower()

            reason = None
            if "study" in title or "interview" in title or "study" in selftext or "interview" in selftext:
                reason = "Contains 'study' or 'interview'"
            elif len(selftext.strip()) < 150:
                reason = "Too short"
            elif post.score < 5:
                reason = "Low score"
            elif post.num_comments < 3:
                reason = "Low comment count"
            elif detect(selftext) != "en":
                reason = "Not English"

            if reason:
                errors.append({
                    "title": post.title,
                    "reason": reason,
                    "score": post.score,
                    "comments": post.num_comments
                })
                continue

            filtered.append(post)

        except Exception as e:
            errors.append({
                "title": getattr(post, "title", "unknown"),
                "reason": f"Exception: {str(e)}",
                "score": getattr(post, "score", "unknown"),
                "comments": getattr(post, "num_comments", "unknown")
            })

    logger.info(f"✅ {len(filtered)} posts passed filter, {len(errors)} skipped.")
    log_activity("Filtering complete", "save_data", f"{len(filtered)} kept / {len(errors)} skipped")

    if errors:
        pd.DataFrame(errors).to_csv("error_log.csv", index=False)
        log_activity("Saved error log", "save_data", "File: error_log.csv")

    return filtered

def save_to_csv(submissions, logger, filename="technostress_posts.csv"):
    filtered_submissions = clean_and_filter(submissions, logger)

    # ✅ Sanity check before proceeding
    if not filtered_submissions:
        logger.warning("No data to save after filtering.")
        log_activity("No posts to save", "save_data", "Filtered data is empty.")
        return

    # ✅ Build the data list
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
    logger.info(f"📁 Saved {len(data)} posts to {filename}")
    log_activity("Saved filtered posts", "save_data", f"File: {filename}")
