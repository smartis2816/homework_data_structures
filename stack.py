class Stack:
    head = None
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
        current = self.head
        if current is not None:
            node.next = self.head
        self.head = node
        self.length += 1

    # Удаление узла
    def pop(self):
        current = self.head
        if current is not None:
            value = current.value
            if current.next is not None:
                self.head = current.next
            else:
                self.head = None
            self.length -= 1
            return value
        print('Стек пуст')
        return None

    # Очистка стека
    def clear_stack(self):
        self.head = None
        self.length = 0

    # Вывод на экран
    def output(self):
        if self.is_empty():
            print('Список пуст')
            return
        node = self.head
        while node.next:
            print(node, end=' ')
            node = node.next
        print(node)

    # Проверка на пустоту
    def is_empty(self):
        return self.head is None
