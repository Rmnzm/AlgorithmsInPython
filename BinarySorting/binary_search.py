# Бинарный поиск
def binary_search(list, item):  # low and high хранят границы части списка в которой выполняется поиск
    low = 0
    high = len(list) - 1

    while low <= high:          # пока часть не сократится до одного элемента
        mid = (low + high)      # проверка среднего элемента
        guess = list[mid]
        if guess == item:       # значение найдено
            return mid
        elif guess > item:      # много
            high = mid - 1
        else:                   # мало
            low = mid + 1
        #return None
