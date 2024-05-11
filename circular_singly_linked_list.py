class CircularSinglyLinkedList:
    head = None
    length = 0

    class Node:
        value = None
        next = None

        def __init__(self, value=None, next_node=None):
            self.value = value
            self.next = next_node

        def __str__(self):
            return str(self.value)

    # вставка узла в начало списка (условное, так как список кольцевой)
    def push_front(self, value):
        node = self.Node(value)
        current = self.head
        if current is None:
            self.head = node
            self.head.next = self.head
            self.length += 1
        else:
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head
            self.head = node
            self.length += 1

    # вставка узла в конец списка (условный, так как список кольцевой)
    def push_back(self, value):
        node = self.Node(value)
        current = self.head
        if current is None:
            self.head = node
            self.head.next = self.head
            self.length += 1
        else:
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head
            self.length += 1

    # вывод списка на экран
    def output(self):
        if self.is_empty():
            print('Список пуст')
            return
        print(self.head, end='\n\n')
        node = self.head.next
        while node != self.head:
            print(node, end='\n\n')
            node = node.next
        print('\n\n')

    # проверка на пустоту
    def is_empty(self):
        return self.head is None

    # очистка списка
    def clear_list(self):
        self.head = None
        self.length = 0

    # поиск узла по занчению, возвращает узел
    def find(self, value):
        current = self.head
        while current.next != self.head:
            if current.value == value:
                return current
            current = current.next
        if current.next == self.head:
            if current.value == value:
                return current
        return None

    # вставка узла по указанному индексу
    def insert(self, value, index):
        if index == 0:
            self.push_front(value)
        elif index == self.length:
            self.push_back(value)
        else:
            node_1, node_2 = self.head, self.head.next
            indicator = 0
            while indicator < index - 1 and node_2 != self.head:
                node_1, node_2 = node_2, node_2.next
                indicator += 1
            node_1.next = self.Node(value, next_node=node_2)
            self.length += 1

    # удаление последнего узла
    def pop_back(self):
        if self.head:
            current = self.head
            if current.next == current:
                self.head, self.length = None, 0
                return
            while current.next.next != self.head:
                current = current.next
            current.next = self.head
            self.length -= 1
        else:
            print('Список пуст')

    # удаление первого узла
    def pop_front(self):
        if self.head:
            current = self.head
            if current.next == current:
                self.head, self.length = None, 0
                return
            while current.next != self.head:
                current = current.next
            self.head = current.next.next
            current.next = self.head
            self.length -= 1
        else:
            print('Список пуст')

    # реверсирование списка
    def reverse(self):
        if self.head and self.head.next != self.head:
            node_1 = None
            node_2 = self.head
            node_3 = node_2.next
            while node_2.next != self.head:
                node_2.next = node_1
                node_1 = node_2
                node_2 = node_3
                node_3 = node_2.next
            node_2.next = node_1
            self.head.next = node_2
            self.head = node_2

    # сортировка списка (reverse=False - по возрастанию, reverse=True - по убыванию)
    def sort(self, reverse=False):
        if self.head is None or self.head.next is self.head:
            return
        tail = self.head
        while tail.next != self.head:
            tail = tail.next
        counter = 0
        while counter < self.length:
            current = self.head
            if reverse is False:
                while current.next != tail.next:
                    following = current.next
                    if current.value > following.value:
                        current.value, following.value = following.value, current.value
                    current = following
                counter += 1
            else:
                while current.next != tail.next:
                    following = current.next
                    if current.value < following.value:
                        current.value, following.value = following.value, current.value
                    current = following
                counter += 1

    # конвертация списка в массив, возвращает массив
    def convert_to_array(self):
        result = []
        current = self.head
        while True:
            result.append(current.value)
            if current.next == self.head:
                break
            current = current.next
        return result

    def show(self):
        if self.is_empty():
            print('Список пуст')
            return
        print(self.head, end=' ')
        node = self.head.next
        while node != self.head:
            print(node, end=' ')
            node = node.next
        print('\n')


if __name__ == '__main__':
    arr = [9, 5, 7, 10, 4, 5, 1, 1, 5, 8]
    test = CircularSinglyLinkedList()
    # for el in arr:
    #     test.push_back(el)
    test.push_front(10)
    test.push_back(99)
    test.show()
    test.pop_front()
    test.show()
    print(test.head.next)
