class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=' -> ')
        current = current.next


node2 = ListNode(2)
node1 = ListNode(1, node2)

printLinkedList(node1)

print()

node_series2_3 = ListNode(5)
node_series2_2 = ListNode(4, node_series2_3)
node_series2_1 = ListNode(3, node_series2_2)

printLinkedList(node_series2_1)