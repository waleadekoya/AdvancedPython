import itertools
from typing import Union, Iterable, Generator

import json_stream


def count(
        start: Union[int, float] = 0,
        step: Union[int, float] = 1,
        stop: Union[int, float] = None
):
    """
    :param start:
    :param step:
    :param stop:
    :return:
    >>> list(count(10, 2.5, 20))
    [10, 12.5, 15.0, 17.5]
    """
    n = start
    while stop is not None and n < stop:
        yield n
        n += step


def square(iterable: Iterable[int]) -> Generator:
    """
    Generator wrapping iterables
    :param iterable:
    :return: Genrator
    >>> list(square(range(5)))
    [0, 1, 4, 9, 16]
    >>> type(square(range(5)))
    <class 'generator'>
    """
    return (item * item for item in iterable)


def odd(iterable: Iterable[int]):
    """
    Example of chaining generators
    :param iterable:
    :return:
    >>> list(square(odd(range(10))))
    [1, 9, 25, 49, 81]
    """
    for i in iterable:
        if i % 2:
            yield i


def padded_square(iterable: Iterable[int]):
    """
    Example of adding extra yield statements outside a loop
    :param iterable:
    :return:
    >>> list(padded_square(range(5)))
    ['start', 0, 1, 4, 9, 16, 'end']
    """
    yield 'start'
    for item in iterable:
        yield item * item
    yield 'end'


def wrap_results_of_multiple_generators():
    """
    :return:
    >>> wrap_results_of_multiple_generators()
    [1, 3, 5, 7, 9]
    """
    import itertools
    result = itertools.count()
    sliced_odd = itertools.islice(odd(result), 5)
    return list(sliced_odd)


class CountGenerator:

    def __init__(self,
                 start: Union[int, float] = 0,
                 step: Union[int, float] = 1,
                 stop: Union[int, float] = None
                 ):
        """
        :param start:
        :param step:
        :param stop:
        >>> list(CountGenerator(start=2.5, step=0.5, stop=5))
        [2.5, 3.0, 3.5, 4.0, 4.5]
        >>> counter = CountGenerator(start=2.5, step=0.5, stop=5)

        # Pretty representation using '__repr__'
        >>> counter
        CountGenerator(start=2.5, step=0.5, stop=5)

        # Check if item exists using '__contains__'
        >>> 3.1 in counter
        True
        >>> 1 in counter
        False
        """
        self.i = start
        self.start = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop is not None and self.i >= self.stop:
            raise StopIteration()
        value = self.i
        self.i += self.step
        return value

    def __len__(self):
        return int((self.stop - self.start) // self.step)

    def __contains__(self, key):
        return self.start < key < self.stop

    def __repr__(self):
        return (
            f'{self.__class__.__name__}(start={self.start}, '
            f'step={self.step}, stop={self.stop})'
        )

    def __getitem__(self, slice_):
        return itertools.islice(self, slice_.start, slice_.stop, slice_.step)


def chunker(iterable, chunk_size):
    # Make sure `iterable` is an iterator
    iterable = iter(iterable)
    while True:
        # Because islice doesn't know how if the iterable has
        # been exhausted, we need to manually check here. Alternatively
        try:
            value = next(iterable)
        except StopIteration:
            return
        else:
            sliced = itertools.islice(iterable, chunk_size - 1)
            # Chain the pre-fetched value and the slice
            yield itertools.chain([value], sliced)


with open("sample.json") as f:
    data = json_stream.load(f)
    # print(data["results"])
    chunks = chunker(data["results"].persistent(), 2)
    for result in chunks:
        data_set = [dict(value) for value in result]
        print(data_set)
        # for i, value in enumerate(result):
        #     print(i, dict(value))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
