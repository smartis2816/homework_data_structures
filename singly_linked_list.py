class SinglyLinkedList:
    head = None

    class Node:
        value = None
        next = None

        def __init__(self, value=None, next_node=None):
            self.value = value
            self.next = next_node

        def __str__(self):
            return str(self.value)

    # Добавление узла в начало
    def push_front(self, value):
        node = self.Node(value)
        current = self.head
        if current is not None:
            node.next = self.head
        self.head = node

    # Добавление узла в конец
    def push_back(self, value):
        node = self.Node(value)
        current = self.head
        if current is None:
            self.head = node
        else:
            while current.next is not None:
                current = current.next
            current.next = node

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

    # Реверсивный вывод на экран
    def output_reverse(self, node):
        if node is None:
            print('Список пуст')
            return
        self.output_reverse(node.next)
        print(node, end=' ')

    # Поиск по значению
    def find(self, value):
        current = self.head
        while current is not None:
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
        node_1.next = self.Node(value, next_node=node_2)

    # Удаление с конца
    def pop_back(self):
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                current = self.head
                while current.next and current.next.next:
                    current = current.next
                current.next = None
        else:
            print('Список пуст')

    # Удаление с начала
    def pop_front(self):
        if self.head and self.head.next:
            self.head = self.head.next
        elif self.head and self.head.next is None:
            self.clear_list()
        else:
            print('Список пуст')

    # Разворот списка
    def reverse(self):
        if self.head and self.head.next:
            node_1 = None
            node_2 = self.head
            while node_2:
                node_3 = node_2.next
                node_2.next = node_1
                node_1 = node_2
                node_2 = node_3
            self.head = node_1

    # Сортировка
    def sort(self, reverse=False):
        if self.head is None or self.head.next is None:
            return
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            current = self.head
            if reverse is False:
                while current.next:
                    if current.value > current.next.value:
                        current.value, current.next.value = current.next.value, current.value
                        is_sorted = False
                    current = current.next
            else:
                while current.next:
                    if current.value < current.next.value:
                        current.value, current.next.value = current.next.value, current.value
                        is_sorted = False
                    current = current.next

    # Очистка листа
    def clear_list(self):
        self.head = None

    # Проверка на пустоту
    def is_empty(self):
        return self.head is None
