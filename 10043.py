class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def detect_cycle_start(head):
    slow = head
    fast = head

    # Шаг 1: Определяем, есть ли цикл
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # цикла нет

    # Шаг 2: Находим начало цикла
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # указатель на начало цикла

# Пример с циклом
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c  # цикл начинается в c

cycle_start = detect_cycle_start(a)
print(cycle_start.value if cycle_start else "null")  # Вывод: 3
