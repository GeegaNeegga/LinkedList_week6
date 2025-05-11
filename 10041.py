class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_reversed(head):
    stack = []
    current = head
    while current:
        stack.append(current.value)
        current = current.next
    while stack:
        print(stack.pop())

# Пример: создаём список 1 -> 2 -> 3
node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)

print_reversed(node1)  # Вывод: 3 2 1 (каждое число на новой строке)
