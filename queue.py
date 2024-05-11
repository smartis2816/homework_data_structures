class Queue:
    head = None
    tail = None
    length = 0

    class Node:
        value = None
        next = None

        def __init__(self, value=None):
            self.value = value
            self.next = None

        def __str__(self):
            return str(self.value)

    # Добавление узла
    def push(self, value):
        node = self.Node(value)
        if self.tail is not None:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
        self.tail = node

    # Удаление узла
    def pop(self):
        if self.is_empty():
            return None
        value = self.head.value
        if self.head.next is None:
            self.head, self.tail = None, None
            self.length = 0
        else:
            self.head = self.head.next
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

