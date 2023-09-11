# ID посылки 90157271
def input_data():
    with open('input.txt', 'r') as f:
        count = int(f.readline())
        data = list(int(_) for _ in f.readline().split())
    return count, data


def search_empty(first, datal):
    """ Поиск пустого участка """
    for index, value in enumerate(datal, start=first+1):
        if value == 0:
            return index-1
    return len(datal)*2


def distance_calculation(count, data):
    """ расчёт дистанции до ближайших пустых участков """
    output = [0] * count
    """ Расчёт первого участка """
    item = 0
    empty = search_empty(item, data)
    output[item] = empty - item
    """ Расчёт остальных участков """
    item += 1
    while item < count:
        empty = search_empty(item, data[item:])+item
        while item <= min(count - 1, empty):
            previous = output[item - 1]
            output[item] = min(empty - item, previous+1)
            item += 1
            if item < count and data[item] == 0:
                empty = item
    return output


if __name__ == '__main__':
    print(*distance_calculation(*input_data()))
