# Простой словарь с проверкой тех кто голосовал

voted = {}  # Создается пустой словарь для голосовавших людей


# Функция проверки голосовал/нет
def check_voter(name):
    if voted.get(name):  # Если голосовавший уже есть в списке, печать сообщения "Выгнать"
        print('Kick them out!')
    else:  # Если голосовавшего нет в списках, печать сообщения "Добро" и допуск к голосованию с занесением в словарь
        voted[name] = True
        print('Let them vote!')


check_voter('tom')

check_voter('mike')

check_voter('mike')
