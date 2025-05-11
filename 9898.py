class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def sum_linked_list(head):
    total = 0
    current = head
    while current:
        total += current.value
        current = current.next
    return total

# Пример ввода: создание списка 1 -> 2 -> 3
node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)

print(sum_linked_list(node1))  # Вывод: 6
