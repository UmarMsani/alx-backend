#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Caching system with LFU (Least Frequently Used) eviction policy.
    """

    def __init__(self):
        """
        Initialize the LFUCache object.
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The value associated with the key.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_frequency = min(self.frequency.values())
                    items_with_min_frequency = [
                        k for k, v in self.frequency.items()
                        if v == min_frequency
                    ]
                    lru_key = min(
                        items_with_min_frequency,
                        key=lambda k: self.cache_data[k]
                    )
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD:", lru_key)
                self.cache_data[key] = item
                self.frequency[key] = 1

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if key doesn't exist
        """
        if key is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
                return self.cache_data[key]
        return None
