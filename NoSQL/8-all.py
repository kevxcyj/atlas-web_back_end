#!/usr/bin/env python3
""" list_all function """

def list_all(mongo_collection):
    """ Lists all documents in collection """
    return list(mongo_collection.find()) if mongo_collection is not None else []
