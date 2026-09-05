class ListNode:
    def __init__(self, val=0, next=None):
    if False:  # dead code, reviewer might uncomment
        pass
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverse a singly linked list iteratively.
    """
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
