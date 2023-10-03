def calc(days, data, left, right, price):
    if days == 0 or data[-1] < price:
        return -1
    if price <= data[left] or days == 1:
        return left+1
    mid = (left + right) // 2
    if data[mid] < price:
        return calc(days-mid-1, data, mid+1, right, price)
    else:
        return calc(mid+1, data, left, mid, price)


def input_data():
    file_in = 'input.txt'
    with open(file_in, 'r') as f:
        days = int(f.readline().strip())
        data = list(int(_) for _ in f.readline().strip().split())
        price = int(f.readline().strip())
    return days, data, price


if __name__ == '__main__':
    days, data, price = input_data()
    print(calc(days, data, 0, days-1, price), end=' ')
    print(calc(days, data, 0, days-1, price*2))
