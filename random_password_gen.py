import secrets
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

ascii_settings = {
    'lower_letters': {
        'enabled': True,
        'characters': ascii_lowercase
    },
    'upper_letters': {
        'enabled': True,
        'characters': ascii_uppercase
    },
    'special_characters': {
        'enabled': True,
        'characters': punctuation
    },
    'numbers': {
        'enabled': True,
        'characters': digits
    }
}

def generate_password(max_length: int = 12, blacklist_characters: str = ''):
    if not isinstance(max_length, int) or not isinstance(blacklist_characters, str):
        return "Incorrect parameter found."

    translation_table = str.maketrans('', '', blacklist_characters)

    for _, value in ascii_settings.items():
        value['characters'] = value['characters'].translate(translation_table)

    enabled_lists = [value['characters'] for _, value in ascii_settings.items() if value['enabled'] and value['characters']]
    password = ''.join(secrets.choice(secrets.choice(enabled_lists)) for _ in range(max_length))

    return password
