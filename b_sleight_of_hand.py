# ID посылки 90399123

def input_data():
    data: list[str] = []
    with open('input.txt', 'r') as f:
        k = int(f.readline())
        for _ in range(4):
            data.extend(max('0', _) for _ in list(f.readline()))
    return k, data


def score(k, data):
    t = int(max(data))
    score = sum((0 < data.count(str(game)) <= k*2)
                for game in range(1, t+1))
    return score


if __name__ == '__main__':
    print(score(*input_data()))
