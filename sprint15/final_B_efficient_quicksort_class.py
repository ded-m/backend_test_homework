#  ID посылки 93685115

class Member:
    def __init__(self, name, amount, penalty):
        self.name = name
        self.amount = amount
        self.penalty = penalty

    def __lt__(self, other):
        return ((-self.amount, self.penalty, self.name) <
                (-other.amount, other.penalty, other.name))

    def __str__(self):
        return self.name


def quicksort(array, start, end):
    def _partition(array, middle, left, right):
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
    if end <= start:  # базовый случай
        return
    # рекурсивный случай
    middle = array[(start + end) // 2]
    left, right = _partition(array, middle, start, end)
    quicksort(array, start, right)
    quicksort(array, left, end)


def input_data():
    member_count = int(input())
    entry = list(map(lambda item: Member(item[0], int(item[1]), int(item[2])),
                 (input().split() for i in range(member_count))))
    return entry


if __name__ == '__main__':
    entry = input_data()
    quicksort(entry, 0, len(entry) - 1)
    [print(member) for member in entry]
