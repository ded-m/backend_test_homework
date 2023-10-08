def add(output, item):
    if range(max(output[-1][0], item[0]), min(output[-1][1], item[1])+1, 1):
        output[-1][0] = min(output[-1][0], item[0])
        output[-1][1] = max(output[-1][1], item[1])
    else:
        output.append(item)
    return output


def input_data():
    file_in = 'input.txt'
    data = []
    with open(file_in, 'r') as f:
        count = int(f.readline().strip())
        for i in range(count):
            data.append(list(int(_) for _ in f.readline().strip().split()))
    return data


if __name__ == '__main__':
    data = sorted(input_data())
    output = [data[0],]
    for item in data[1:]:
        output = add(output, item)
    for item in output:
        print(*item)
