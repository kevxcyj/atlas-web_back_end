#!/usr/bin/env python3

""" BasiCache class """

from base_caching import BaseCaching


class BasicCache(BaseCaching):

    """ Inherits from BC and is a Caching system """

    def put(self, key, item):
        """ Put the item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Grab the item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
