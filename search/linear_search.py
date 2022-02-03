#!/usr/bin/env python3
from random import Random


r = Random()
unsorted_list = [r.randint(1, 10) for _ in range(10)]
print(unsorted_list)


def linear_search(unsorted_list: list, item_for_search: int) -> bool:
    """
    It is Linear search function, it's good for unsorted lists.
    """
    for item in unsorted_list:
        if item == item_for_search:
            return True
    return False


item_for_search = r.randint(1, 10)
result = linear_search(unsorted_list, item_for_search)
print(f"{item_for_search} is in unsorted_list {result}")
