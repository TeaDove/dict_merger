from copy import deepcopy
import pytest
from tests import shared


class TestClass:
    @pytest.mark.parametrize("dict_merger_impl", shared.mergers)
    def test_merge(self, dict_merger_impl):
        original_a = deepcopy(shared.a)

        result = dict_merger_impl.merge(shared.a, shared.b)

        assert shared.a == original_a
        assert result == shared.a_b_merge

    @pytest.mark.parametrize("dict_merger_impl", shared.mergers)
    def test_merge_inplace(self, dict_merger_impl):
        a = deepcopy(shared.a)

        result = dict_merger_impl.merge_inplace(a, shared.b)

        assert result is None
        assert a == shared.a_b_merge

    @pytest.mark.parametrize("dict_merger_impl", shared.mergers)
    def test_merge_many(self, dict_merger_impl):
        original_a = deepcopy(shared.a)

        result = dict_merger_impl.merge_many([shared.a, shared.b, shared.c])

        assert original_a == shared.a
        assert result == shared.a_b_c_merge
