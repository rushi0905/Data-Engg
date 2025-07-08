def remove_duplicate_word(str):
    words = str.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)
input_str = "this is a test this is only a test"
output_str = remove_duplicate_word(input_str)
print(output_str)
