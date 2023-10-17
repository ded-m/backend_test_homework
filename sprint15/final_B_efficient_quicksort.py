def partition(array, middle, left, right):
    while left <= right:
        while array[left] < middle:
            left += 1
        while middle < array[right]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left, right


def quicksort(array, start, end):
    if end <= start:  # базовый случай,
        return
    else:  # рекурсивный случай
        middle = array[(start+end)//2]
        left, right = partition(array, middle, start, end)
        quicksort(array, start, right)
        quicksort(array, left, end)


def input_data():
    file_in = 'input.txt'
    with open(file_in, 'r') as f:
        n = int(f.readline().strip())
        entry = list(map(lambda item: [int(item[1]), -int(item[2]), item[0]],
                         (f.readline().strip().split() for i in range(n))))
    return entry


if __name__ == '__main__':
    entry = input_data()
    quicksort(entry, 0, len(entry)-1)
    print(entry)
