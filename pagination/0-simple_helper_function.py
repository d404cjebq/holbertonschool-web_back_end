#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Module that provides a simple helper function for pagination.

This module contains a function to compute the start and end
indexes of a page, based on the page number and the page size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end indexes for a given pagination.

    Given a 1-indexed page number and a page size, this function
    calculates the corresponding start index and end index that
    can be used to slice a dataset (e.g. a list) in order to
    retrieve the items of that specific page.

    Args:
        page (int): The page number (1-indexed, first page is 1).
        page_size (int): The number of items expected per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and
        the end index for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
