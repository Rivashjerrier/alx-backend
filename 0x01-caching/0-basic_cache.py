#!/usr/bin/env python3
""" 0-basic_cache.py """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache  inherits from BaseCaching and is a caching system """

    def put(self, key, item):
        """ Adds item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets an item by key in the cache """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
