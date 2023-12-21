#!/usr/bin/env python3
""" Return tuple"""


def index_range(page: int, page_size: int) -> tuple:
    """Provide a tuple with two elements, 
representing the starting and ending indices 
that correspond to the range of indexes to be
 retrieved from a list based on specific pagination parameters """
    myTuple = ((page - 1) * page_size, page * page_size)
    return (myTuple)
