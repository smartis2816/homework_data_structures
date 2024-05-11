class DoublyLinkedList:
    head = None
    tail = None

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

    # Добавление узла в конец
    def push_back(self, value):
        node = self.Node(value)
        if self.tail is not None:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node

    # Добавление узла в начало
    def push_front(self, value):
        node = self.Node(value)
        if self.head is not None:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = node

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

    # Реверсивный вывод на экран
    def output_reverse(self):
        if self.is_empty():
            print('Список пуст')
            return
        node = self.tail
        while node:
            print(node, end=' ')
            node = node.prev
        print('\n')

    # Проверка на пустоту
    def is_empty(self):
        return self.head is None

    # Разворот списка
    def reverse(self):
        if self.head is None or self.head.next is None:
            return
        temp = self.head
        self.head = self.tail
        self.tail = temp
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.next

    # Поиск по значению
    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    # Вставка по индексу
    def insert(self, value, index):
        node_1, node_2 = self.head, self.head
        indicator = 0
        while indicator < index:
            node_1, node_2 = node_2, node_2.next
            indicator += 1
        node_1.next = self.Node(value, next_node=node_2, prev_node=node_1)

    # Удаление с конца
    def pop_back(self):
        if self.is_empty():
            return
        if self.tail.prev is None:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # Удаление с начала
    def pop_front(self):
        if self.is_empty():
            return
        if self.head.next is None:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Очистка листа
    def clear_list(self):
        self.head = None

    # Сортировка
    def sort(self, reverse=False):
        if self.head is None or self.head.next is None:
            return
        marker = None
        while marker != self.head:
            current = self.head
            if reverse is False:
                while current.next != marker:
                    following = current.next
                    if current.value > following.value:
                        current.value, following.value = following.value, current.value
                    current = current.next
                marker = current
            else:
                while current.next != marker:
                    following = current.next
                    if current.value < following.value:
                        current.value, following.value = following.value, current.value
                    current = current.next
                marker = current
