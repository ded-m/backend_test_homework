#  ID посылки 91497957
OPERATIONS = {'+': lambda x, y: x+y,
              '-': lambda x, y: x-y,
              '*': lambda x, y: x*y,
              '/': lambda x, y: x//y,
              }


class Stack:
    def __init__(self):
        self.__stack = []

    def add(self, x):
        self.__stack.append(int(x))

    def pop(self):
        return self.__stack.pop()


def input_data():
    return input().strip().split()


def calculation(data):
    stack = Stack()

    for item in data:
        if item.isdigit() or item[1:].isdigit():
            stack.add(item)
        else:
            y = stack.pop()
            x = stack.pop()
            stack.add(OPERATIONS[item](x, y))
    return stack.pop()


if __name__ == '__main__':
    print(calculation(input_data()))
