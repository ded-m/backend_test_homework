def is_first_item_bigger(item_1, item_2):  # функция-компаратор
    return item_1 > item_2


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array, large):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор large
        while j > 0 and large(item_to_insert + array[j-1], array[j-1] + item_to_insert):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    return array


def input_data():
    file_in = 'input.txt'
    with open(file_in, 'r') as f:
        count = f.readline().strip()
        sequence = list(f.readline().strip().split())
    return count, sequence


if __name__ == '__main__':
    count, sequence = input_data()
    print(''.join(insertion_sort_by_comparator(sequence, is_first_item_bigger)))
