class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Пример: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
middle = find_middle_node(head)
print(middle.value)  # Вывод: 3

# Пример: 1 -> 2 -> 3 -> 4
head2 = Node(1, Node(2, Node(3, Node(4))))
middle2 = find_middle_node(head2)
print(middle2.value)  # Вывод: 3 (второй из двух середины)
