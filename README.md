# Dict merger
Simple Cython+Python library for merge python dictionaries recursively
[PyPi](https://pypi.org/project/dict-merger/)
### Usage

```python
from dict_merger.static_merger import merge

a = {1: 2, 2: 3, 3: {1: 1, 2: 3}, 4: 1}
b = {1: 5, 3: {1: 2}, 5: 3}

print(merge(a, b))
# {1: 5, 2: 3, 3: {1: 2, 2: 3}, 4: 1, 5: 3}
```

### API
```python
# dict_merger.static_merger - pure Cython module with static python types
# dict_merger.dynamic_merger - same module, but with dynamic types, works a bit slower

def merge(first_dict: dict, second_dict: dict) -> dict:
    """
    Merge 2 dicts recursively. If more than one given map or object defines the same key or attribute,
    then the one that is later in the argument sequence takes precedence.
    :param first_dict:
    :param second_dict:
    :return:
    """
    ...

def merge_inplace(first_dict: dict, second_dict: dict) -> None:
    """
    Merge 2 dicts recursively. If more than one given map or object defines the same key or attribute,
    then the one that is later in the argument sequence takes precedence.
    First dict will contain merged version
    """
    ...

def merge_many(dicts: List[dict]) -> dict:
    """
    Merge list of dicts. If more than one given map or object defines the same key or attribute,
    then the one that is later in the argument sequence takes precedence.
    :param dicts: list of dicts
    :return: dict
    """
    ...
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


### Credits
For any questions, suggestions etc write peter.ibragimov@gmail.com or to telegram: [@teadove](https://t.me/teadove)
