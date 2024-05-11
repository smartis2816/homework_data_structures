class BinaryTree:
    root = None

    def __init__(self, root):
        self.root = self.Node(root)

    class Node:
        value = None
        left = None
        right = None

        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.value)

    # Добавление узла в дерево
    def add(self, value):
        node = self.Node(value)
        if self.root is None:
            root = node
        else:
            current = self.root
            while current is not None:
                if value < current.value:
                    if current.left is None:
                        current.left = node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    current = current.right

    # Поиск по значению
    def find(self, value):
        if self.root is not None:
            current = self.root
            while current is not None:
                if current.value == value:
                    return current
                elif value < current.value:
                    current = current.left
                else:
                    current = current.right
        return None

    # Проверка на пустоту
    def is_empty(self):
        return self.root is None

    # Вывод на экран
    def output(self, node: Node):
        if node is not None:
            self.output(node.left)
            print(node.value, end=' ')
            self.output(node.right)


if __name__ == '__main__':
    test = BinaryTree(10)
    test.add(3)
    test.add(13)
    test.add(7)
    test.add(4)
    test.add(15)
    test.add(11)
    test.output(test.root)
