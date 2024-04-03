#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Caching system with LRU (Least Recently Used) eviction policy.
    """

    def __init__(self):
        """
        Initialize the LRUCache object.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The value associated with the key.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.queue.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.queue.append(key)
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
            if key in self.cache_data:
                self.queue.remove(key)
                self.queue.append(key)
                return self.cache_data[key]
        return None
