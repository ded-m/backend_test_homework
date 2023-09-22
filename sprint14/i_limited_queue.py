class MyQueueSized():
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        if self.length != self.max_n:
            self.queue[self.tail] = x
        else:
            return 'error'
        self.tail = (self.tail + 1) % self.max_n
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.length -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        return self.length


def input_data():
    commands = []
    # count = int(input())
    # max_size = int(input())
    # for _ in range(count):
    #     commands.append(input().strip().split())

    file_in = 'sprint14/input.txt'
    with open(file_in, 'r') as f:
        count = int(f.readline())
        max_size = int(f.readline())
        for _ in range(count):
            commands.append(f.readline().strip().split())

    return max_size, commands


if __name__ == '__main__':
    max_size, commands = input_data()
    queue = MyQueueSized(max_size)
    output = []
    for command in commands:
        if command[0] == 'push':
            if queue.push(int(command[1])) == 'error':
                output.append('error')
        if command[0] == 'pop':
            output.append(queue.pop())
        if command[0] == 'peek':
            output.append(queue.peek())
        if command[0] == 'size':
            output.append(queue.size())
    for item in output:
        print(item)
