#!/usr/bin/env python3

""" FIFOCache class """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    """ Inhereits from BC and is a caching system """
    
    def put(self, key, item):
        """ Put the item in the cache"""
        if key is None or item is None:
            return 
        self.cache_data[key] = item

    def get(self, key):
        """ Grab the item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
