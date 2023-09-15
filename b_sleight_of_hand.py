# ID посылки 90579424

def input_data():
    k = int(input())
    data = input()+input()+input()+input()
    return k, data


def score(k, data):
    t = int(max(data))
    score = sum((0 < data.count(str(game)) <= k*2)
                for game in range(1, t+1))
    return score


if __name__ == '__main__':
    print(score(*input_data()))
