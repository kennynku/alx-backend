#!/usr/bin/env python3
""" Return tuple"""

import csv
import math
from typing import List


class Server:
    """paginate a database of popular baby names.
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
        """Simple pagination"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        idx = index_range(page, page_size)
        try:
            return self.dataset()[idx[0]:idx[1]]
        except IndexError:
            return []


def index_range(page: int, page_size: int) -> tuple:
    """ Provide a tuple with two elements,
 representing the starting and ending indices
 that correspond to the range of indexes to be 
retrieved from a list based on specific pagination parameters """

    myTuple = ((page - 1) * page_size, page * page_size)
    return (myTuple)
