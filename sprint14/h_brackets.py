def is_correct_bracket_seq(chain):
    bracket_dict = {')': '(', '}': '{', ']': '['}
    brackets = []
    for bracket in chain:
        if (bracket == '(' or bracket == '[' or bracket == '{'):
            brackets.append(bracket)
        elif brackets != [] and bracket_dict[bracket] == brackets[-1]:
            brackets.pop()
        else:
            return False
    if brackets == []:
        return True
    else:
        return False


def input_data():
    # chain = input().strip()
    file_in = 'sprint14/input.txt'
    with open(file_in, 'r') as f:
        chain = f.readline().strip()
    return chain


if __name__ == '__main__':
    print(is_correct_bracket_seq(input_data()))
