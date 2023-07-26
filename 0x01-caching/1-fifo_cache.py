#!/usr/bin/env python3
""" 1-fifo_cache.py """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialiaze """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Adds item in the cache using FIFO algorithm """
        if key and item:
            self.cache_data[key] = item
            self.keys.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.keys[0])
                popped = self.keys.pop(0)
                print("DISCARD: {}".format(popped))

    def get(self, key):
        """ Gets an item by key in the cache """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
