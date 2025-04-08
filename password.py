def has_digit(password):
    return any(bum.isdigit() for bum in password)


def is_very_long(password):
    return not len(password) >= 12



def has_lower_letters(password):
    return any(mub.islower() for mub in password)


def has_upper_letters(password):
    return any(tum.isupper() for tum in password)


def has_symbols(password):
    return any(not cek.isalnum() for cek in password)


def main():
    password = input("Введите пароль: ")
    score = 0

    funktions = [
        has_digit,
        is_very_long,
        has_lower_letters,
        has_upper_letters,
        has_symbols,
    ]

    for funkt in funktions:
        if funkt(password):
            score += 2


    print("Рейтинг пароля:", score)


if __name__ == '__main__':
    main()    








