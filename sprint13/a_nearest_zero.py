# ID посылки 90637311

def input_data():
    count = int(input())
    data = list(int(_) for _ in input().split())
    return count, data


def distance_calculation(count, data):
    output = [0] * count
    empty = -1
    for index, value in enumerate(data):
        if value == 0:
            if empty >= 0:
                median = int((index-empty)//2)
                output[index-median:index] = output[empty+median:empty:-1]
            elif index > 0:
                output[:index] = output[index-1::-1]
            empty = index
        else:
            output[index] = index - empty
    return output


if __name__ == '__main__':
    print(*distance_calculation(*input_data()))
