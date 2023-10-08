COMBO_DICT = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


def generator(sequence, chain):
    if sequence == []:
        print(chain, end = ' ')
    else:
        for item in COMBO_DICT[sequence[0]]:
            generator(sequence[1:], chain+item)


if __name__ == '__main__':
    sequence = list(int(_) for _ in list(input()))
    generator(sequence, '')
