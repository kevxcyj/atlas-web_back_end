#!/usr/bin/env python3

""" FIFOCache class """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    
    def put(self, key, item):
        if key is None or item is None:
            return 
        self.cache_data[key] = item

    def get(self, key, item):
        if key is None or key not in self.cache_data:
            return None
            return self.cache_data.get(key)
