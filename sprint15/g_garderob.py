def input_data():
    # file_in = 'input.txt'
    # with open(file_in, 'r') as f:
    #     count = int(f.readline().strip())
    #     sequence = list(int(_) for _ in f.readline().strip().split())
    count = int(input())
    sequence = list(int(_) for _ in input().split())
    return count, sequence


def sort(sequence, count):
    counted_values = [0] * count
    for value in sequence:
        counted_values[value] += 1

    for value in range(count):
        print((str(value) + ' ') * counted_values[value], end='')


if __name__ == '__main__':
    count, sequence = input_data()
    if count > 1:
        sort(sequence, 3)
    else:
        print(*sequence)
