def bubble_sort(sequence):
    flag = 1
    for item in range(len(sequence)-1):
        if sequence[item] > sequence[item+1]:
            sequence[item], sequence[item+1] = sequence[item+1], sequence[item]
            flag = 0
    return sequence, flag


def input_data():
    file_in = 'input.txt'
    with open(file_in, 'r') as f:
        count = f.readline().strip()
        sequence = list(int(_) for _ in f.readline().strip().split())
    return count, sequence


if __name__ == '__main__':
    count, sequence = input_data()
    flag = 0
    q = 0
    while flag == 0:
        sequence, flag = bubble_sort(sequence)
        if flag == 0:
            print(*sequence)
            q = 1
    if q == 0:
        print(*sequence)