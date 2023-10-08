def generator(count, chain, l_bracket, r_bracket):
    if l_bracket == count and r_bracket == count:
        print(chain)
    else:
        if l_bracket < count:
            generator(count, chain+'(', l_bracket + 1, r_bracket)
        if r_bracket < l_bracket:
            generator(count, chain+')', l_bracket, r_bracket + 1)


if __name__ == '__main__':
    count = int(input())
    generator(count, '', 0, 0)
