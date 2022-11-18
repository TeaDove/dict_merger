# Dict merger
Simple Cython+Python library for merge python dictionaries recursively
[PyPi](https://pypi.org/project/dict-merger/)
### Usage

```python
from dict_merger.static_merger import merge

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

merge(a, b) == {
    1: 5,
    2: 3,
    3: {1: 2, 2: 3},
    4: 1,
    5: 3,
}
# P.S: If more than one given dict defines the same key,
# then the one that is later in the argument sequence takes precedence.
```

### API
```python
# dict_merger.static_merger - pure Cython module with static python types
# dict_merger.dynamic_merger - same module, but with dynamic types, works a bit slower

def merge(first_dict: dict, second_dict: dict) -> dict:
    """
    Merge 2 dicts recursively.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.
    :param first_dict: first dict to merge
    :param second_dict: second dict to merge
    :return: merged dict
    """
    ...

def merge_inplace(first_dict: dict, second_dict: dict) -> None:
    """
    Merge 2 dicts recursively.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.

    First dict will contain merged version, faster in general.
    :param first_dict: first dict to merge, will contain merged version
    :param second_dict: second dict to merge
    """
    ...

def merge_many(dicts: List[dict]) -> dict:
    """
    Merge list of dicts.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.
    :param dicts: list of dicts
    :return: merged dict
    """
    ...

def merge_many_inplace(dicts: List[dict]) -> None:
    """
    Merge list of dicts inplace
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.

    :param dicts: list of dicts
    """
```

#### Installation
```shell
# via pypi
pip install dict_merger

# via git
pip install git+https://github.com/TeaDove/dict_merger.git #@branch/tag

# build locally
git clone https://github.com/TeaDove/dict_merger.git #@branch/tag
cd dict_merger
make install
```

### Performance tests
```pycon
dict_merger.static_merger - cython mergers with static types
dict_merger.dynamic_merger - cython mergers with dynamic types
tests.pure_python - pure python implementation mergers

test_merge_inplace_random[dict_merger.static_merger] 101.64757675000146
test_merge_inplace_random[dict_merger.dynamic_merger] 111.33557962499981
test_merge_inplace_random[tests.pure_python] 346.21198354100125

test_merge_static[dict_merger.static_merger] 4.421063124998909
test_merge_static[dict_merger.dynamic_merger] 4.379016041999421
test_merge_static[tests.pure_python] 4.7141847090024385

test_merge_inplace_static[dict_merger.static_merger] 0.21805158300048788
test_merge_inplace_static[dict_merger.dynamic_merger] 0.2745717500001774
test_merge_inplace_static[tests.pure_python] 0.6025681659994007

test_merge_many_static[dict_merger.static_merger] 4.533137833001092
test_merge_many_static[dict_merger.dynamic_merger] 4.706059832999017
test_merge_many_static[tests.pure_python] 5.675890833001176

test_merge_many_inpace_static[dict_merger.static_merger] 0.42021320900312276
test_merge_many_inpace_static[dict_merger.dynamic_merger] 0.572701542001596
test_merge_many_inpace_static[tests.pure_python] 1.5192962910005008
```

### Credits
For any questions, suggestions etc. write peter.ibragimov@gmail.com or to telegram: [@teadove](https://t.me/teadove)
