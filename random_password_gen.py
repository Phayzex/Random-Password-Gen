import secrets
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

ascii_bool_map = {
    'lower_letters': True,
    'upper_letters': True,
    'special_characters': True,
    'numbers': True
}

ascii_map = {
    'lower_letters': ascii_lowercase,
    'upper_letters': ascii_uppercase,
    'special_characters': punctuation,
    'numbers': digits
}

def generate_password(max_length: int = 12, blacklist_characters: str = ''):
    if not isinstance(max_length, int) or not isinstance(blacklist_characters, str):
        return "Incorrect parameter found."

    translation_table = str.maketrans('', '', blacklist_characters)

    for k, v in ascii_map.items():
        ascii_map[k] = v.translate(translation_table)

    enabled_lists = [ascii_map[key] for key, value in ascii_bool_map.items() if value and ascii_map[key]]
    password = ''.join(secrets.choice(secrets.choice(enabled_lists)) for _ in range(max_length))

    return password
