def diff_count(string_a, string_b):
    validate(string_a, string_b)
    return len([[x,y] for x, y in zip(string_a, string_b) if x != y])

def validate(string_a, string_b):
    if len(string_a) != len(string_b):
        raise ValueError('Length of both string_a and string_b must be equal')
