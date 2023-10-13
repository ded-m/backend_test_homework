def partition(array, pivot, left1, right1):
    left = [int(array[left1][1]), int(array[left1][2]), array[left1][0]]
    right = [int(array[right1][1]), int(array[right1][2]), array[right1][0]]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left, right

def quicksort(array, start, end):
    if len(array) < 2:  # базовый случай,
        return       # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = int(len(array)/2)
        # pivot = array[random.randint(start, end)]

        left, right = partition(array, pivot, start, end)
        quicksort(array, start, right)
        quicksort(array, left, end)

def input_data():
    file_in = 'input.txt'
    with open(file_in, 'r') as f:
        n = int(f.readline().strip())
        entry = [f.readline().strip().split() for i in range(n)]
    return entry

if __name__ == '__main__':
    entry = input_data()
    quicksort(entry, 0, len(entry)-1)
    print(entry)
