#  ID посылки 91099563

class Deque:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push_back(self, x):
        if self.length != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.length += 1
        else:
            return 'error'

    def push_front(self, x):
        if self.length != self.max_n:
            self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = x
            self.length += 1
        else:
            return 'error'

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.length -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.length -= 1
        return x


def input_data():
    commands = []
    # count = int(input())
    # deque_max = int(input())
    # for _ in range(count):
    #     commands.append(input().strip().split())
    file_in = 'sprint14/input.txt'
    with open(file_in, 'r') as f:
        count = int(f.readline())
        deque_max = int(f.readline())
        for _ in range(count):
            commands.append(f.readline().strip().split())
    return deque_max, commands


if __name__ == '__main__':
    deque_max, commands = input_data()
    stack = Deque(deque_max)
    output = []
    for command in commands:
        if command[0] == 'push_back':
            if stack.push_back(int(command[1])) == 'error':
                output.append('error')
        if command[0] == 'push_front':
            if stack.push_front(int(command[1])) == 'error':
                output.append('error')
        if command[0] == 'pop_back':
            output.append(stack.pop_back())
        if command[0] == 'pop_front':
            output.append(stack.pop_front())
    for item in output:
        print(item)
