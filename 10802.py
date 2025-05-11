class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_cycle_start(head):
    slow = fast = head

    # 1. Обнаружение цикла
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return -1  # Цикл не найден

    # 2. Нахождение начала цикла
    slow = head  # Перемещаем один указатель в начало
    steps = 0
    while slow != fast:
        slow = slow.next
        fast = fast.next
        steps += 1

    return steps

# Пример: создаём список с циклом
# 1 -> 2 -> 3 -> 4
#           ^    |
#           |____|

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n4.next = n3  # цикл

print(find_cycle_start(n1))  # Вывод: 2 (цикл начинается с узла 3, на расстоянии 2 от начала)
