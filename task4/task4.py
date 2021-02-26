import string


def caesar(text, step, alphabets):
    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_alphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_alphabets, joined_shifted_alphabets)
    return text.translate(table)


if __name__ == '__main__':
    print(caesar("Hello, world! Привет, мир!", 2, (string.ascii_lowercase,
                                                   string.ascii_uppercase, string.digits,
                                                   'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                                                   'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')))
