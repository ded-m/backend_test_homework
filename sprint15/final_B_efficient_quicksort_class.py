#  ID посылки 93490596

class member():
    def __init__(self, name, amount, penalty):
        self.name = name
        self.amount = amount
        self.penalty = penalty

    def __lt__(self, other):
        return (-self.amount, self.penalty, self.name) < \
               (-other.amount, other.penalty, other.name)


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
        entry = []
        for i in range(n):
            name, amount, penalty = f.readline().strip().split()
            entry.append(member(name, int(amount), int(penalty)))
    return entry


if __name__ == '__main__':
    entry = input_data()
    quicksort(entry, 0, len(entry)-1)
    [print(member.name) for member in entry]
