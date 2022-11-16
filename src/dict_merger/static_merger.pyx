from copy import deepcopy

__all__ = ["merge", "merge_inplace", "merge_many"]


cdef dict _rmerge(dict first_dict, dict second_dict, list path):
    """
    Recursive merging utility

    :param first_dict: first dict to merge, used as result
    :param second_dict: dict to merge with
    :param path: current dict path
    """
    for key in second_dict:
        if (
            key in first_dict
            and isinstance(first_dict[key], dict)
            and isinstance(second_dict[key], dict)
        ):
            _rmerge(first_dict[key], second_dict[key], path + [str(key)])
        else:
            first_dict[key] = second_dict[key]
    return first_dict


cdef dict merge(dict first_dict, dict second_dict):
    """
    Merge 2 dicts recursively.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.
    :param first_dict: first dict to merge
    :param second_dict: second dict to merge
    :return: merged dict
    """
    return _rmerge(deepcopy(first_dict), second_dict, list())



cdef void merge_inplace(dict first_dict, dict second_dict):
    """
    Merge 2 dicts recursively.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.

    First dict will contain merged version, faster in general.
    :param first_dict: first dict to merge, will contain merged version
    :param second_dict: second dict to merge
    """
    _rmerge(first_dict, second_dict, list())

cdef dict merge_many(list dicts):
    """
    Merge list of dicts.
    If more than one given dict defines the same key,
    then the one that is later in the argument sequence takes precedence.
    :param dicts: list of dicts
    :return: merged dict
    """
    if len(dicts) < 2:
        raise Exception("List len should be at least 2")
    cdef dict to_return = merge(dicts[0], dicts[1])
    for i in range(2, len(dicts)):
        to_return = merge(to_return, dicts[i])
    return to_return
