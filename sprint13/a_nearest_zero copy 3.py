# ID посылки 90523321

def input_data():
    with open('input.txt', 'r') as f:
        count = int(f.readline())
        data = list(int(_) for _ in f.readline().split())
    return count, data


def distance_calculation(data_temp, output_temp):
    enum = float('inf')
    for index, value in enumerate(data_temp):
        if value == 0:
            enum = 0
            output_temp[index] = 0
        else:
            enum += 1
            output_temp[index] = min(enum, output_temp[index])
    return output_temp


def main(count, data):
    output = [float('inf')] * count
    output = distance_calculation(data, output)
    output = list(reversed(distance_calculation(list(reversed(data)),
                                                list(reversed(output)))))
    return output


if __name__ == '__main__':
    print(*main(*input_data()))
