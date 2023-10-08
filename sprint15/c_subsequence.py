def contained(subsequence, sequence):
    if subsequence == '':
        return True
    i = -1
    for item in subsequence:
        i = sequence.find(item, i + 1)
        if i == - 1:
            return False
    return True


def input_data():
    file_in = 'input.txt'
    with open(file_in, 'r') as f:
        subsequence = f.readline().strip()
        sequence = f.readline().strip()
    return subsequence, sequence


if __name__ == '__main__':
    subsequence, sequence = input_data()
    print(contained(subsequence, sequence))
