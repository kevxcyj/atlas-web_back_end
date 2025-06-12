#!/usr/bin/env python3
""" schools_by_topic function """

def schools_by_topic(mongo_collection, topic):
    """ Return list of schools having a specific topic. """
    return list(mongo_collection.find({"topics": topic}))
