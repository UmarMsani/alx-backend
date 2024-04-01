#!/usr/bin/env python3
"""
index_range module
"""

from typing import Tuple, List, Dict, Union
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index
            for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves the requested page of data from the dataset.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: The requested page of data, or an empty list if
                the input arguments are out of range for the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]

    def get_hyper(
            self,
            page: int = 1,
            page_size: int = 10
            ) -> Dict[str, Union[int, List[List], None]]:
        """
        Returns a dictionary containing hypermedia pagination information.

        Args:
            page (int): The page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            Dict[str, Union[int, List[List], None]]: A dictionary containing
                pagination information.
        """
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_data = {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
        return hyper_data
