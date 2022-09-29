import os
from heapq import nsmallest, nlargest
from pathlib import Path
from functools import partial, reduce
from heapq import heappush
from operator import mul, add
from itertools import accumulate
from pprint import pprint
from typing import List, Any, Dict

directories = list(filter(os.path.isdir, Path(r'C:\Users\chezy\OneDrive\Mortgage').glob("*")))

heap = []
push = partial(heappush, heap)
smallest = partial(nsmallest, iterable=heap)
largest = partial(nlargest, iterable=heap)

push(1)
push(3)
push(5)
push(2)
push(4)
print(smallest(3))
print(largest(2))

print(reduce(mul, range(1, 10)))


def cum_sum(iterable: List[int]):
    """ accumulate – reduce with intermediate results
    >>> cum_sum([10, 8, 5, 7, 12, 10, 5, 8, 15, 3, 4, 2])
    [10, 18, 23, 30, 42, 52, 57, 65, 80, 83, 87, 89]
    """
    from itertools import accumulate
    from operator import add
    return list(accumulate(iterable, add))


def combine_multiple_iterators(*iterable: List[Any]):
    """
    :param iterable:
    :return:
    >>> combine_multiple_iterators(smallest(3), largest(2))
    [1, 2, 3, 5, 4]
    >>> combine_multiple_iterators(smallest(3), ["boy", "apple", "zoo", "elephant", "table", "drugs"])
    [1, 2, 3, 'boy', 'apple', 'zoo', 'elephant', 'table', 'drugs']
    """
    from itertools import chain
    return list(chain(*iterable))


def group_iterable(iterable: List[Any], key: callable) -> Dict[Any, Any]:
    """
    :param iterable: the list of items to group (must be sorted)
    :param key: the callable to use for group key
    :return: a dictionary where the key is the groupby key and the value is the list of grouped items
    >>> raw_items = ['spam', 'eggs', 'sausage', 'spam', 'toilet']
    >>> group_iterable(raw_items, key=lambda x: x[0])
    {'e': ['eggs'], 's': ['sausage', 'spam', 'spam'], 't': ['toilet']}
    """
    from itertools import groupby
    iterable.sort()
    return {group: list(items) for group, items in groupby(iterable, key=key)}


if __name__ == "__main__":
    import doctest
    doctest.testmod()
