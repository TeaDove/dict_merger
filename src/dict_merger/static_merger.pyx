from copy import deepcopy


def _rmerge(dict first_dict, dict second_dict, list path):
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


def merge(dict first_dict, dict second_dict) -> dict:
    """
    Merge 2 dicts recursively. If more than one given map or object defines the same key or attribute,
    then the one that is later in the argument sequence takes precedence.
    :param first_dict:
    :param second_dict:
    :return:
    """
    return _rmerge(deepcopy(first_dict), second_dict, list())



def merge_inplace(dict first_dict, dict second_dict) -> None:
    """
    Merge 2 dicts recursively. If more than one given map or object defines the same key or attribute,
    then the one that is later in the argument sequence takes precedence.
    First dict will contain merged version
    """
    _rmerge(first_dict, second_dict, list())

def merge_many(list dicts) -> dict:
    """
    Merge list of dicts. If more than one given map or object defines the same key or attribute,
    then the one that is later in the argument sequence takes precedence.
    :param dicts: list of dicts
    :return: dict
    """
    if len(dicts) < 2:
        raise Exception("List len should be at least 2")
    cdef dict to_return = merge(dicts[0], dicts[1])
    for i in range(2, len(dicts)):
        to_return = merge(to_return, dicts[i])
    return to_return
