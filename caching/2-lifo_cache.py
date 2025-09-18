#!/usr/bin/env python3

""" LIFOCache class """


from base_caching import BaseCaching


class LIFOCache(BaseCaching):

    """ Caching systm with LIFO, inherites from BC """

    def __init__(self):
        """ Initialization """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Put the item in the cache """
        if key is None or item is None:
            return
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = list(self.cache_data.keys())[0]
            del self.cache_data[oldest_key]
            print(f'DISCARD: {oldest_key}')

        self.cache_data[key] = item

    def get(self, key):
        """ Grab the item from the cache """
        if key is None:
            return None
        
        return self.cache_data.get(key)