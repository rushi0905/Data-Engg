def remove_duplicate_Char(str):
    """
    Remove duplicate characters from a string while preserving the order of first occurrences.

    :param str: Input string from which duplicates need to be removed
    :return: String with duplicates removed
    """
    seen = set()
    result = []

    for char in str:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)
print(remove_duplicate_Char('ababababa'))