class Deque:
    head = None
    tail = None
    length = 0

    class Node:
        value = None
        next = None
        prev = None

        def __init__(self, value=None, next_node=None, prev_node=None):
            self.value = value
            self.next = next_node
            self.prev = prev_node

        def __str__(self):
            return str(self.value)

    # Добавление узла в начало
    def push_front(self, value):
        node = self.Node(value)
        if self.head is not None:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    # Добавление узла в конец
    def push_back(self, value):
        node = self.Node(value)
        if self.tail is not None:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    # Удаление узла в конце
    def pop_back(self):
        if self.is_empty():
            return None
        value = self.head.value
        if self.tail.prev is None:
            self.head, self.tail = None, None
            self.length = 0
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        return value

    # Удаление узла в начале
    def pop_front(self):
        if self.is_empty():
            return None
        value = self.head.value
        if self.head.next is None:
            self.head, self.tail = None, None
            self.length = 0
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        return value

    # Вывод на экран
    def output(self):
        if self.is_empty():
            print('Список пуст')
            return
        node = self.head
        while node:
            print(node, end=' ')
            node = node.next
        print('\n')

    # Проверка на пустоту
    def is_empty(self):
        return self.head is None

    # Очистка очереди
    def clear_queue(self):
        self.head, self.tail = None, None
        self.length = 0
