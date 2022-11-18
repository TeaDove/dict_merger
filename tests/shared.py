import dict_merger
from tests import pure_python

mergers = [dict_merger.static_merger, dict_merger.dynamic_merger, pure_python]
a = {
    1: 2,
    2: 3,
    3: {1: 1, 2: 3},
    4: 1,
}
b = {
    1: 5,
    3: {1: 2},
    5: 3,
}
c = {2: 5, 3: {1: 2, 3: 5}, 5: 3}
a_b_merge = {
    1: 5,
    2: 3,
    3: {1: 2, 2: 3},
    4: 1,
    5: 3,
}
a_b_c_merge = {1: 5, 2: 5, 3: {1: 2, 2: 3, 3: 5}, 4: 1, 5: 3}
iterations = 1_000_000
