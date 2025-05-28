#!/usr/bin/env python3
""" Cache system using LRU """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Put function """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = min(self.cache_data, key=lambda x: self.cache_data[x])
            del self.cache_data[lru_key]
            print(f'DISCARD: {lru_key}')

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
