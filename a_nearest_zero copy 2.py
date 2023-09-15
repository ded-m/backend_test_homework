# ID посылки 90157271
def input_data():
    with open('input.txt', 'r') as f:
        count = int(f.readline())
        data = list(int(_) for _ in f.readline().split())
    return count, data


def search_empty(first, tail):
    """ Поиск пустого участка """
    for index, value in enumerate(tail):
        if value == 0:
            return index
    return len(tail)*2


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
            output[item] = min(empty - item, output[item - 1]+1)
            item += 1
    return output


if __name__ == '__main__':
    print(*distance_calculation(*input_data()))
