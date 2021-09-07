
# поиск индекса наименьшего элемента

def findSmallest(lst):
    smallest = lst[0]                   # Для хранения наименьшего значения
    smallest_index = 0                  # Для хранения индекса наименьшего значения

    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            smallest_index = i
    return smallest_index

# алгоритм сортировки выбором

def simpleSort(lst):                    # Сортирует список
    newLst = []

    for i in range(len(lst)):
        smallest = findSmallest(lst)    # Находит наименьший элемент в списке и добавляет его в новый список
        newLst.append(lst.pop(smallest))
    return newLst