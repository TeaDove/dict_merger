from copy import deepcopy
from typing import List, Mapping, MutableMapping, Sequence, Union


def _rmerge(first_dict: Union[MutableMapping, Mapping], second_dict: Mapping, path: List[str]) -> Mapping:
    """
    Recursive merging utility

    :param first_dict: first dict to merge, used as result
    :param second_dict: dict to merge with
    :param path: current dict path
    """
    for key in second_dict:
        if key in first_dict and isinstance(first_dict[key], dict) and isinstance(second_dict[key], dict):
            _rmerge(first_dict[key], second_dict[key], path + [str(key)])
        else:
            first_dict[key] = second_dict[key]
    return first_dict


def merge(first_dict: Mapping, second_dict: Mapping) -> Mapping:
    """
    Merge 2 dicts recursively.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.
    :param first_dict: first dict to merge
    :param second_dict: second dict to merge
    :return: merged dict
    """
    return _rmerge(deepcopy(first_dict), second_dict, list())


def merge_inplace(first_dict: MutableMapping, second_dict: Mapping) -> None:
    """
    Merge 2 dicts recursively.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.

    First dict will contain merged version, faster in general.
    :param first_dict: first dict to merge, will contain merged version
    :param second_dict: second dict to merge
    """
    _rmerge(first_dict, second_dict, list())


def merge_many(dicts: Sequence[MutableMapping]) -> Mapping:
    """
    Merge list of dicts.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.
    :param dicts: list of dicts
    :return: merged dict
    """
    if len(dicts) < 2:
        raise Exception("List len should be at least 2")
    to_return = merge(dicts[0], dicts[1])
    for i in range(2, len(dicts)):
        to_return = merge(to_return, dicts[i])
    return to_return


def merge_many_inplace(dicts: Sequence[MutableMapping]) -> None:
    """
    Merge list of dicts.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.
    :param dicts: list of dicts
    :return: merged dict
    """
    if len(dicts) < 2:
        raise Exception("List len should be at least 2")

    consumer_dict = dicts[0]
    merge_inplace(consumer_dict, dicts[1])
    for i in range(2, len(dicts)):
        merge_inplace(consumer_dict, dicts[i])