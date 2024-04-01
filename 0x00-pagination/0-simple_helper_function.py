#!/usr/bin/env python3
"""
index_range module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple containing start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index and end index
            for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
