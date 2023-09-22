class MyQueueSized():
    def __init__(self):
        self.queue = []
        self.head = 0
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def put(self, x):
        self.queue.append(x)
        self.length += 1

    def get(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1
        self.length -= 1
        return x

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
        for _ in range(count):
            commands.append(f.readline().strip().split())
    return commands


if __name__ == '__main__':
    commands = input_data()
    queue = MyQueueSized()
    output = []
    for command in commands:
        if command[0] == 'put':
            queue.put(int(command[1]))
        if command[0] == 'get':
            output.append(queue.get())
        if command[0] == 'size':
            output.append(queue.size())
    for item in output:
        print(item)
