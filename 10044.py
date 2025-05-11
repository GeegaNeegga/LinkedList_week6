class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(l1, l2):
    dummy = Node(0)  # Временный старт
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Прицепляем остатки
    tail.next = l1 if l1 else l2

    return dummy.next  # Первый реальный элемент

# Пример: 1->3->5 и 2->4->6
a1 = Node(1, Node(3, Node(5)))
a2 = Node(2, Node(4, Node(6)))

merged = merge_sorted_lists(a1, a2)

# Печать результата
current = merged
while current:
    print(current.value, end=' ')
    current = current.next
# Вывод: 1 2 3 4 5 6
