import json
from dataclasses import dataclass
from pprint import pprint
from typing import List, Dict, Any
import builtins
from collections import ChainMap, OrderedDict, defaultdict
from enum import Enum


@dataclass
class Group:
    name: str
    parent: 'Group' = None


@dataclass
class User:
    username: str
    email: str = None
    role: str = None
    groups: List[Group] = None


class CRMUser(User):
    # Managing Default Argument Values https://realpython.com/python-chainmap/
    def __init__(self, name, component, **kwargs):
        defaults: Dict[str: Any] = {"email": next(component.email), "role": "write"}
        super().__init__(name, **ChainMap(kwargs, defaults))


users = Group('users')
admins = Group('admins', users)
tom = User('rick', groups=[admins])
dave = User('dave', 'dave@simpsons.com', groups=[admins])

numbers = OrderedDict(one=1, two=2)
letters = defaultdict(str, {"a": "A", "b": "B"})

pprint(tom.groups)

builtin_vars = vars(builtins)
# pprint(builtin_vars)
mappings = ChainMap(
    locals(), globals(), builtin_vars
)
chainmap_from_keys = ChainMap.fromkeys(["one", "two", "three"], 0)
pprint(mappings.get("letters"))
pprint(chainmap_from_keys)

# Prioritizing CLI Application Settings
# Order of proxy service for connecting to the internet
# 1. CLI user-provided options 2. Local config files in the user's home directory
# 3. system-wide proxy configuration 4. Defaults
cli_proxy = {}
local_proxy = dict(proxy="proxy.local.com")
system_proxy = dict(proxy="proxy.system.com")
config = ChainMap(cli_proxy, local_proxy, system_proxy)
print(config.get("proxy"))

nodes = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'a'),
    ('b', 'd'),
    ('c', 'a'),
    ('d', 'a'),
    ('d', 'b'),
    ('d', 'c'),
]

graph = defaultdict(list)
for from_, to in nodes:
    graph[from_].append(to)

print(graph)


def tree():
    return defaultdict(tree)


colours = tree()
colours['other']['black'] = 0x000000
colours['other']['white'] = 0xFFFFFF
colours['primary']['red'] = 0xFF0000
colours['primary']['green'] = 0x00FF00
colours['primary']['blue'] = 0x0000FF
colours['secondary']['yellow'] = 0xFFFF00
colours['secondary']['aqua'] = 0x00FFFF
colours['secondary']['fuchsia'] = 0xFF00FF

print(json.dumps(colours, sort_keys=True, indent=4))


class Color(int, Enum):
    red = 1
    green = 2
    blue = 3


class Spam(str, Enum):
    EGGS = 'eggs'


print(Color.red == 1, Spam.EGGS == "eggs")


def sort_collections_using_heapq(iterable: List[Any]):
    from heapq import heapify, heappop
    heapify(iterable)  # Transforms list into a heap (sorted as a tree), in-place, in O(len(heap)) time
    print(iterable)
    while iterable:
        print(heappop(iterable), iterable)


def heapsort(iterable: List[Any]):
    # the heapsort algorithm
    from heapq import heappush, heappop
    heap = []
    for item in iterable:
        heappush(heap, item)  # Push item onto heap, maintaining the heap invariant

    # To get the sorted version of the heap, we keep removing the top of the tree until all the items are gone
    while heap:
        yield heappop(heap)


sort_collections_using_heapq([1, 3, 5, 7, 2, 4, 3])

print(list(heapsort([1, 3, 5, 7, 2, 4, 3])))
print(list(heapsort(["boy", "apple", "zoo", "elephant", "table", "drugs"])))


def binary_search_algorithm(sorted_list: List[Any], value: Any) -> bool:
    # best if the collection is already sorted or use heapsort to first sort it
    from bisect import bisect_left
    i = bisect_left(sorted_list, value)
    return i < len(sorted_list) and sorted_list[i] == value


print(binary_search_algorithm(list(range(1000000)), 30000))

# https://github.com/python/cpython/blob/master/Lib/collections/__init__.py
