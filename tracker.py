import os
import csv
from datetime import datetime

def log_activity(action, source="system", notes=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = [timestamp, action, source, notes]
    file_exists = os.path.isfile("activity_log.csv")

    with open("activity_log.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Action", "Source", "Notes"])
        writer.writerow(log_entry)
