#!/usr/bin/env python3
"""
Module that implements hypermedia pagination over a dataset of
popular baby names read from a CSV file.
"""
import csv
import math
from typing import List, Dict, Any

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a new Server instance with an empty cache."""
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
        """Return the requested page of the dataset.

        Args:
            page (int): The page number to retrieve (1-indexed).
                Must be a positive integer.
            page_size (int): The number of items per page.
                Must be a positive integer.

        Returns:
            List[List]: The list of rows corresponding to the
            requested page. Returns an empty list if the page
            or page_size are out of range for the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dictionary with pagination metadata (hypermedia).

        Args:
            page (int): The page number to retrieve (1-indexed).
                Must be a positive integer.
            page_size (int): The number of items per page.
                Must be a positive integer.

        Returns:
            Dict[str, Any]: A dictionary containing:
                - page_size: the length of the returned dataset page
                - page: the current page number
                - data: the dataset page itself
                - next_page: the number of the next page, or None
                - prev_page: the number of the previous page, or None
                - total_pages: the total number of pages in the dataset
        """
        data = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
        }
