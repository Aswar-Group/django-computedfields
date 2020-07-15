from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def modelname(model):
    return '%s.%s' % (model._meta.app_label, model._meta.verbose_name)


def is_sublist(needle, haystack):
    if not needle:
        return True
    if not haystack:
        return False
    max_k = len(needle) - 1
    k = 0
    for elem in haystack:
        if elem != needle[k]:
            k = 0
            continue
        if k == max_k:
            return True
        k += 1
    return False


def parent_to_inherited_path(parent, inherited):
    """
    Pull relation path segments from `parent` to `inherited` model
    in multi table inheritance.
    """
    bases = inherited._meta.get_base_chain(parent)
    relations = []
    model = inherited
    for base in bases:
        relations.append(model._meta.parents[base].remote_field.name)
        model = base
    return relations[::-1]
