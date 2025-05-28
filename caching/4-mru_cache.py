#!/usr/bin/env python3

""" MRU Caching system """

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRU Cache class """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Put fucntion """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = max(self.cache_data, key=lambda x: self.cache_data[x])
            del self.cache_data[mru_key]
            print(f'DISCARD: {mru_key}')

        self.cache_data[key] = item

    def get(self, key):
        """ Get function """
        if key is None:
            return None

        if key in self.cache_data:
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
        return None