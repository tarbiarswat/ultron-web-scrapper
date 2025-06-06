import logging

def setup_logger(name="RedditScraper"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs if re-imported
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

        # File handler
        fh = logging.FileHandler("scraper.log")
        fh.setFormatter(formatter)

        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
