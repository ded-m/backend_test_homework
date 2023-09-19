# ID посылки 000000
def input_data():
    with open('input.txt', 'r') as f:
        lines_count = int(f.readline())
        columns_count = int(f.readline())
        data = []
        for i in range(lines_count):
            data.append(list(f.readline().split()))
    return lines_count, columns_count, data


def transform(lines_count, columns_count, data):
    output = []
    for __ in range(columns_count):
        for _ in range(lines_count):
            output.append(data[_][__])
        output[__ * lines_count + columns_count] += '\n'
    return output


if __name__ == '__main__':
    print(' '.join(transform(*input_data())))
