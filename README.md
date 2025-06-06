# 🤖 Ultron Web Scraper — Reddit Technostress Intelligence

Ultron is a powerful, modular Python scraper that gathers high-quality Reddit posts related to **technostress**, **digital burnout**, and **technology-induced stress**. It uses both Reddit’s official live API and the Pushshift archive API to pull real-time and historical data, then applies smart filtering, logs all actions, and stores results in a clean, structured CSV — ready for analysis or reporting.

---

## 🚀 Features

- 🔗 Fetches posts from both **Reddit API** and **Pushshift API**
- 🔍 Uses multiple related **keywords** (e.g., "technostress", "burnout")
- 🌐 Detects and keeps **English-only** posts
- 🧹 Filters out:
  - Posts with “study” or “interview” in title or text
  - Posts with less than 150 characters
  - Posts with low interaction (score < 5, comments < 3)
- 📊 Tracks all activity in `activity_log.csv`
- ⚠️ Logs skipped posts and reasons in `error_log.csv`
- 📁 Exports clean results to `technostress_posts.csv`
- 📓 Outputs debug logs to `scraper.log`

---

## 📁 Project Structure

```plaintext
ultron-web-scrapper/
├── config.py              # Stores Reddit API credentials
├── fetch_reddit.py        # Pulls posts using Reddit's official PRAW API
├── fetch_pushshift.py     # Pulls historical posts using Pushshift API
├── logger.py              # Sets up logger for console and file output
├── save_data.py           # Filters, cleans, saves valid posts to CSV
├── tracker.py             # Logs all actions to activity_log.csv
├── run_scraper.py         # Orchestrates scraping, filtering, saving
├── scraper.log            # Debug and execution logs
├── error_log.csv          # Skipped posts with reasons
├── activity_log.csv       # Tracked user/system actions
├── technostress_posts.csv # Final clean dataset
├── requirements.txt       # All dependencies
└── README.md              # This documentation
