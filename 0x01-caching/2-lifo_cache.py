#!/usr/bin/env python3
""" 2-lifo_cache.py  """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialiaze """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Adds item in the cache using LIFO algorithm """
        if key and item:
            self.cache_data[key] = item
            self.keys.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = len(self.keys) - 2
                discard = self.keys.pop(last_key)
                del self.cache_data[discard]
                print("DISCARD: " + discard)

    def get(self, key):
        """ Gets an item by key in the cache """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
