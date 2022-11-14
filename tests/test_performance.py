import timeit
import random
from copy import deepcopy
from tests import shared
import pytest


class TestClass:
    def gen_dict(self, n, depth=0, max_depth=5):
        dict_ = {}
        for i in range(n):
            if random.randint(0, 1) or depth >= max_depth:
                dict_[i] = random.randint(0, 10)
            else:
                dict_[i] = self.gen_dict(random.randint(0, 10), depth + 1, max_depth)
        return dict_

    @pytest.mark.parametrize("dict_merger_impl", shared.mergers)
    def test_merge_static(self, dict_merger_impl):
        globals_ = globals()
        globals_["dict_merger_impl"] = dict_merger_impl

        print(
            timeit.timeit(
                "dict_merger_impl.merge(shared.a, shared.b)",
                globals=globals_,
                number=shared.iterations,
            )
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
            )
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
            )
        )
