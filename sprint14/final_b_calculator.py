#  ID посылки xxx

class Stack:
    def __init__(self, data):
        self.stack = data
        self.head = 0
        self.length = 0

    def is_empty(self):
        return self.length == 0
    
    def next(self):
        self.head += 1

    def shift(self, res):
        self.stack[self.head] = None
        self.stack[self.head + 1] = None
        self.stack[self.head + 2] = str(res)
        self.head += 2

    def addition(self):
        res = int(self.stack[self.head - 2]) + int(self.stack[self.head - 1])
        self.shift(res)

    def subtraction(self):
        res = int(self.stack[self.head - 2]) - int(self.stack[self.head - 1])
        self.shift(res)

    def multiplication(self):
        res = int(self.stack[self.head - 2]) * int(self.stack[self.head - 1])
        self.shift(res)

    def division(self):
        res = int(self.stack[self.head - 2]) // int(self.stack[self.head - 1])
        self.shift(res)


def input_data():
    file_in = 'sprint14/input.txt'
    with open(file_in, 'r') as f:
        data = f.readline().strip().split()
        # data = input().strip().split()
    return data


if __name__ == '__main__':
    data = input_data()
    stack = Stack(data)
    for item in stack.stack:
        if item == '+':
            stack.addition()
        if item == '-':
            stack.subtraction()
        if item == '*':
            stack.multiplication()
        if item == '/':
            stack.division()

    print(stack.stack[stack.head])
