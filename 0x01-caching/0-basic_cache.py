#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching system without limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The value associated with the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key,
            or None if the key doesn't exist.
        """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
