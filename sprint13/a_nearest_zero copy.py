# ID посылки 90157271
def input_data():
    with open('input.txt', 'r') as f:
        count = int(f.readline())
        data = list(map(int, f.readline().split()))
    return count, data


# Поиск пустого участок
def search_null(first):
    for i in range(first, count):
        if data[i] == 0:
            return i
    return count*2


# Основной блок
if __name__ == '__main__':
    count, data = input_data()
    output = [0] * count
    # Расчёт первого участка
    item = 0
    empty = search_null(item) + item
    output[item] = empty - item
    # Расчёт остальных участков
    item += 1
    while item < count:
        empty = search_null(item)
        while item <= min(count - 1, empty):
            previous = output[item - 1]
            output[item] = min(empty - item, previous+1)
            item += 1
            if item < count and data[item] == 0:
                empty = item
    print(' '.join(map(str, output)))
