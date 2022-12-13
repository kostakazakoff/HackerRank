def validate_str(string: str):
    check = {
        'any_alphanumeric': False,
        'any_alpha': False,
        'any_digits': False,
        'any_lowercase': False,
        'any_uppercase': False
    }
    for char in string:
        if char.isalnum(): check['any_alphanumeric'] = True
        if char.isalpha(): check['any_alpha'] = True
        if char.isdigit(): check['any_digits'] = True
        if char.islower(): check['any_lowercase'] = True
        if char.isupper(): check['any_uppercase'] = True

    [print(x) for x in check.values()]


if __name__ == '__main__':
    s = input()
    validate_str(s)