class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def remove_cycle(head):
    slow = fast = head

    # 1. Обнаружение цикла
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return  # Цикл не найден

    # 2. Поиск начала цикла
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # 3. Найти последний узел цикла и разорвать
    ptr = slow
    while ptr.next != slow:
        ptr = ptr.next
    ptr.next = None

# Пример: создаём список с циклом
# 1 -> 2 -> 3 -> 4
#           ^    |
#           |____|

n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n4.next = n3  # цикл

remove_cycle(n1)

# Проверка: печать списка (цикла быть не должно)
cur = n1
while cur:
    print(cur.value, end=' ')
    cur = cur.next
# Вывод: 1 2 3 4
