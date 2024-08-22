#!/usr/bin/env python3
"""
Script to provide some statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def log_stats():
    """
    Prints statistics about Nginx logs.
    """
    # Connect to the MongoDB server
    client = MongoClient('localhost', 27017)

    # Access the logs database and the nginx collection
    db = client.logs
    collection = db.nginx

    # Count the total number of documents
    total_logs = collection.count_documents({})

    # Print the total number of logs
    print(f"{total_logs} logs")

    # Count the number of documents for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of documents with method GET and path /status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
