class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None

    p1, p2 = headA, headB

    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA

    return p1  # либо None, либо узел пересечения

# Пример: создаём пересекающиеся списки
# A: 1 -> 2 \
#             -> 8 -> 9
# B:     3 -> 4 /

common = Node(8, Node(9))
a = Node(1, Node(2, common))
b = Node(3, Node(4, common))

intersection = get_intersection_node(a, b)
print(intersection.value if intersection else "null")  # Вывод: 8
