# Рекурсия
# Функция вызывает сама себя

from numpy import empty


def countdown(i):
    print(i)
    if i <= 0:                              # Базовый случай
        return
    else:
        countdown(i - 1)                    # Рекурсия


countdown(3)                                # Пример


def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('found the key!')


def greet2(name):
    print('how are you, ' + name + '?')


def bye():
    print('ok bye')


def greet(name):
    print('Hello, ' + name + '!')           # Выводитс приветствие
    greet2(name)                            # Блок вызова функции
    print('getting ready to say bye...')    # Следующее сообщение
    bye()                                   # Финальная функция


greet('Sasha')                              # Пример
