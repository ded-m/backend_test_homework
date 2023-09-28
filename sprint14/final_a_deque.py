#  ID посылки 91582282

class Deque:
    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_n = max_size
        self.__head = 0
        self.__tail = 0
        self.__length = 0

    def __is_empty(self):
        return self.__length == 0

    def __is_full(self):
        return self.__length == self.__max_n

    def __index(self, command):
        if command == 'push_back':
            if self.__is_empty():
                self.__head = 0
                self.__tail = 0
                return 0
            return (self.__tail + 1) % self.__max_n
        if command == 'push_front':
            if self.__is_empty():
                self.__head = 0
                self.__tail = 0
                return 0
            return (self.__head - 1) % self.__max_n
        if command == 'pop_front':
            return (self.__head + 1) % self.__max_n
        if command == 'pop_back':
            return (self.__tail - 1) % self.__max_n

    def push_back(self, x):
        if self.__is_full():
            raise IndexError()
        self.__tail = self.__index('push_back')
        self.__queue[self.__tail] = x
        self.__length += 1

    def push_front(self, x):
        if self.__is_full():
            raise IndexError()
        self.__head = self.__index('push_front')
        self.__queue[self.__head] = x
        self.__length += 1

    def pop_front(self):
        if self.__is_empty():
            raise IndexError()
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.__index('pop_front')
        self.__length -= 1
        return x

    def pop_back(self):
        if self.__is_empty():
            raise IndexError()
        x = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.__tail = self.__index('pop_back')
        self.__length -= 1
        return x


if __name__ == '__main__':
    count = int(input())
    deque = Deque(int(input()))
    for _ in range(count):
        try:
            command, *args = input().strip().split()
            output = getattr(deque, command)(*args)
            if 'pop' in command:
                print(output)
        except IndexError:
            print('error')
