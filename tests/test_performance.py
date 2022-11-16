import random
import timeit
from copy import deepcopy

import pytest
from tests import shared


def gen_dict(n, depth=0, max_depth=3):
    dict_ = {}
    for i in range(n):
        if random.randint(0, 1) or depth >= max_depth:
            dict_[i] = random.randint(0, 10)
        else:
            dict_[i] = gen_dict(random.randint(0, 10), depth + 1, max_depth)
    return dict_


def get_items_count(dict_: dict) -> int:
    count = 0
    for key, value in dict_.items():
        if isinstance(value, dict):
            count += get_items_count(value)
        count += 1
    return count


class TestClass:
    @pytest.mark.parametrize("dict_merger_impl", shared.mergers)
    def test_merge_static(self, dict_merger_impl):
        globals_ = globals()
        globals_["dict_merger_impl"] = dict_merger_impl

        print(
            timeit.timeit(
                "dict_merger_impl.merge(shared.a, shared.b)",
                globals=globals_,
                number=shared.iterations,
            ),
            end=" ",
        )

    @pytest.mark.parametrize("dict_merger_impl", shared.mergers)
    def test_merge_inplace_static(self, dict_merger_impl):
        globals_ = globals()
        globals_["dict_merger_impl"] = dict_merger_impl
        a = deepcopy(shared.a)
        globals_["a"] = a

        print(
            timeit.timeit(
                "dict_merger_impl.merge_inplace(a, shared.b)",
                globals=globals_,
                number=shared.iterations,
            ),
            end=" ",
        )

    @pytest.mark.parametrize("dict_merger_impl", shared.mergers)
    def test_merge_many_static(self, dict_merger_impl):
        globals_ = globals()
        globals_["dict_merger_impl"] = dict_merger_impl

        print(
            timeit.timeit(
                "dict_merger_impl.merge_many([shared.a, shared.b, shared.c])",
                globals=globals_,
                number=shared.iterations,
            ),
            end=" ",
        )

    @pytest.mark.parametrize("dict_a, dict_b", [(gen_dict(3), gen_dict(3)) for i in range(4)])
    @pytest.mark.parametrize("dict_merger_impl", shared.mergers)
    def test_merge_inplace_random(self, dict_merger_impl, dict_a, dict_b):
        globals_ = globals()
        globals_["dict_merger_impl"] = dict_merger_impl
        globals_["a"] = dict_a
        globals_["b"] = dict_b

        print(
            f"dict_a: {get_items_count(dict_a)}, dict_b: {get_items_count(dict_b)}",
            timeit.timeit(
                "dict_merger_impl.merge_inplace(a, b)",
                globals=globals_,
                number=shared.iterations,
            ),
            end=" ",
        )
