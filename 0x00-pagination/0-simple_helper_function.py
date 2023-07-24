#!/usr/bin/env python3
"""
0-simple_helper_function.py
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        A tuple containing the start index and end index.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return start_index, end_index
