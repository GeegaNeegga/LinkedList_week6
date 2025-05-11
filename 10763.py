class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def detect_cycle_length(head):
    slow = fast = head

    # 1. Обнаружение цикла
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return -1  # Цикл не найден

    # 2. Вычисление длины цикла
    cycle_length = 0
    current = slow
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break

    return cycle_length

# Пример: создаём список с циклом
# 1 -> 2 -> 3 -> 4
#           ^    |
#           |____|

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n4.next = n3  # цикл

print(detect_cycle_length(n1))  # Вывод: 3 (цикл длиной 3)

