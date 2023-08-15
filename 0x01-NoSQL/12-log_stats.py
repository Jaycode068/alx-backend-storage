#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as example
first line: x logs, x number of documents in this collection
second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
"""

from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, method=None):
    """
    Prototype: def log_stats(mongo_collection, option=None):
    Provide some stats about Nginx logs stored in MongoDB
    """
    result = mongo_collection.count_documents({})
    if result:
        if method:
            print(f"method {method}: {mongo_collection.count_documents({'method': {'$regex': method}})}")
        else:
            print(f"{result} logs")
            print("Methods:")
            for method in METHODS:
                print(f"\t{method}: {mongo_collection.count_documents({'method': method})}")
            print(f"{mongo_collection.count_documents({'path': '/status'})} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)

