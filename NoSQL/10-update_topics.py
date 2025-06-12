#!/usr/bin/env python3
""" update_topics function """

def update_topics(mongo_collection, name, topics):
    """ Update all topics of school document """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
