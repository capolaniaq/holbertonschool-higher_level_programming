def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    value_max = max(a_dictionary.values())
    for i in a_dictionary:
        if a_dictionary[i] == value_max:
            key_max = i
    return key_max
