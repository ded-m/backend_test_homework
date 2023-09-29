#  ID посылки 91639306

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

    def __index(self, index, command, direction):
        if command == 'push':
            if self.__is_empty():
                self.__head = 0
                self.__tail = 0
                return 0
        return (index + direction) % self.__max_n

    def push_back(self, item):
        if self.__is_full():
            raise IndexError()
        self.__tail = self.__index(self.__tail, 'push', 1)
        self.__queue[self.__tail] = item
        self.__length += 1

    def push_front(self, item):
        if self.__is_full():
            raise IndexError()
        self.__head = self.__index(self.__head, 'push', -1)
        self.__queue[self.__head] = item
        self.__length += 1

    def pop_front(self):
        if self.__is_empty():
            raise IndexError()
        item = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.__index(self.__head, 'pop', 1)
        self.__length -= 1
        return item

    def pop_back(self):
        if self.__is_empty():
            raise IndexError()
        item = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.__tail = self.__index(self.__tail, 'pop', -1)
        self.__length -= 1
        return item


if __name__ == '__main__':
    count = int(input())
    deque = Deque(int(input()))
    for _ in range(count):
        try:
            command, *args = input().strip().split()
            output = getattr(deque, command)(*args)
            if not args:
                print(output)
        except IndexError:
            print('error')
