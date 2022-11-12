COMMANDS_DICT = {}


def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMMANDS_DICT:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()


def reaction_func(reaction):
    return COMMANDS_DICT.get(reaction, break_func)


def break_func():
    """
    Якщо користувач ввів якусь тарабарщину- повертаємо відповідну відповідь
    :return: Неправильна команда
    """
    return 'Wrong enter.'


def main():
    """
    Основна логика усього застосунку. Отримуємо ввід від користувача
    і відправляємо його в середину застосунку на обробку.
    :return:
    """
    
    while True:
        """
        Просимо користувача ввести команду для нашого бота
        Також тут же вимикаємо бота якщо було введено відповідну команду
        """

        user_input = input('Enter command for bot: ')
        result = change_input(user_input)
        print(result)
        if result == 'good bye':
            break
    


if __name__ == '__main__':
    main()