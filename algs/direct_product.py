import itertools
from typing import Any, Iterable, Tuple


def list_product(groups: Iterable[Tuple[Any]]) -> None:
    """List all combinations of items in groups
    https://ja.wikipedia.org/wiki/%E7%9B%B4%E7%A9%8D%E9%9B%86%E5%90%88

    Args:
        groups (Iterable[tuple[Any]]): Groups
    """

    for prod in itertools.product(*groups):
        print(prod)


if __name__ == "__main__":
    groups = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    list_product(groups)
    # $ python -m algs.direct_product
    # (1, 4, 7)
    # (1, 4, 8)
    # (1, 4, 9)
    # ...
    # (3, 6, 8)
    # (3, 6, 9)