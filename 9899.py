class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def length_linked_list(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

# Пример: создаём список 10 -> 20 -> 30
node3 = Node(30)
node2 = Node(20, node3)
node1 = Node(10, node2)

print(length_linked_list(node1))  # Вывод: 3
