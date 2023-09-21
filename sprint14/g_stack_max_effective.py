class StackMax:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        self.items.append(item)
        if self.max == [] or item >= self.max[-1]:
            self.max.append(item)

    def pop(self):
        if self.items != []:
            if self.max[-1] == self.items[-1]:
                self.max.pop()
            return self.items.pop()
        else:
            return 'error'

    def get_max(self):
        max_value = None
        if self.items != []:
            max_value = self.max[-1]
        return max_value


def input_data():
    commands = []
    # count = int(input())
    # for _ in range(count):
    #     commands.append(input().strip().split())
    # return commands
    file_in = 'sprint14/input.txt'
    with open(file_in, 'r') as f:
        count = int(f.readline())
        for _ in range(count):
            commands.append(f.readline().strip().split())
        return commands


if __name__ == '__main__':
    stack = StackMax()
    output = []
    for command in input_data():
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            if stack.pop() == 'error':
                output.append('error')
        if command[0] == 'get_max':
            output.append(stack.get_max())
    for item in output:
        print(item)
