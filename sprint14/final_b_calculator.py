#  ID посылки 91409944

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, x):
        self.stack.append(int(x))

    def shift(self, res):
        self.stack[-2] = res
        self.stack.pop()

    def addition(self):
        res = self.stack[-2] + self.stack[-1]
        self.shift(res)

    def subtraction(self):
        res = self.stack[-2] - self.stack[-1]
        self.shift(res)

    def multiplication(self):
        res = self.stack[-2] * self.stack[-1]
        self.shift(res)

    def division(self):
        res = self.stack[-2] // self.stack[-1]
        self.shift(res)


def input_data():
    return input().strip().split()


def calculation(data):
    stack = Stack()
    for item in data:
        if item.isdigit() or item[1:].isdigit():
            stack.add(item)
        else:
            if item == '+':
                stack.addition()
            if item == '-':
                stack.subtraction()
            if item == '*':
                stack.multiplication()
            if item == '/':
                stack.division()
    return stack.stack[-1]


if __name__ == '__main__':
    print(calculation(input_data()))
