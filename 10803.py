class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def remove_first_occurrence(head, target):
    current = head
    # Если нужно удалить первый узел
    if current and current.value == target:
        return current.next

    # Проходим по списку, чтобы найти целевой узел
    while current and current.next:
        if current.next.value == target:
            current.next = current.next.next  # Удаляем узел
            return head
        current = current.next
    
    return head  # Если целое число не найдено

# Пример: 1 -> 2 -> 3 -> 4 -> 5
n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

# Удалим первое вхождение 3
head = remove_first_occurrence(n1, 3)

# Печать списка после удаления
current = head
while current:
    print(current.value, end=" ")
    current = current.next
# Вывод: 1 2 4 5
