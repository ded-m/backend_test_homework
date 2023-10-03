def generator(count, chain):
    if count == 0:
        print(chain)
    else:
        generator(count-1, chain+'(')


if __name__ == '__main__':
    count = int(input())
    generator(count, '')
