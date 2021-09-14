# Функция SUM своя собственная, считает что-то :)

def sum_func(*x):
    def flatten(a):
        result = []
        for e in a:
            if isinstance(e, int):
                result.append(e)
            else:
                result.extend(flatten(e))
        return result
    return sum(flatten(x))

print(sum_func([[1,2,[3]],[1],3]))


