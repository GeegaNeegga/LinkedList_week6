class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Пример 1: без цикла
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
print(has_cycle(a))  # False

# Пример 2: с циклом
x = Node(1)
y = Node(2)
z = Node(3)
x.next = y
y.next = z
z.next = y  # цикл здесь
print(has_cycle(x))  # True
