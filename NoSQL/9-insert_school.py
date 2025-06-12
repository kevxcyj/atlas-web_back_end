#!/usr/bin/env python3
""" insert_school function """

def insert_school(mongo_collection, **kwargs):
    """ Inserts a document in a collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
