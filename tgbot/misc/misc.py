from transliterate import translit


def get_translited_username(username: str) -> str:
    username = translit(username, 'ru')
    return ' '.join(map(lambda x: x.title(), username.split(' ')))
