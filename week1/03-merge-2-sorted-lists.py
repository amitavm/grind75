# Leetcode problem 21: Merge Two Sorted Lists
#
# You are given the heads of two sorted linked lists, `list1` and `list2`.
# Merge the two lists into one *sorted* list. The list should be made by
# splicing together the nodes of the first two lists.  Return the head of the
# merged linked list.
#
# Example definition of a singly-linked list:
#
#   class ListNode:
#       def __init__(self, val=0, next=None):
#           self.val = val
#           self.next = next
#
# NOTE: This (solution) is basically a "linked list" version of the merge
# procedure employed in the classic merge-sort algorithm.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(
    list1: ListNode | None,
    list2: ListNode | None
) -> ListNode | None:
    # Create a dummy placeholder so we don't lose our head!
    head = tail = ListNode()

    # The "merge" procedure when both lists have elements left in them.
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # One or both of the lists are exhausted.  Just attach the list with any
    # leftover elements to the end of our result list.
    tail.next = list1 if list1 else list2

    # Return the actual head by discarding the dummy.
    # NOTE that this does the right thing when both list1 and list2 are empty.
    return head.next


# Print a visual representation of a list to stdout.
# (So that we can do some rudimentary manual testing of our solution.)
def printList(head: ListNode | None):
    print('(', end='')
    if head:
        node = head
        print(node.val, end='')
        node = node.next
        while node:
            print(f' -> {node.val}', end='')
            node = node.next
    print(')')


def main():
    list1 = ListNode(1, ListNode(3, ListNode(6, ListNode(7, ListNode(8)))))
    # list1 = None
    print('list1: ', end='')
    printList(list1)

    list2 = ListNode(2, ListNode(5, ListNode(6, ListNode(9))))
    # list2 = None
    print('list2: ', end='')
    printList(list2)

    mlist = mergeTwoLists(list1, list2)
    print('mlist: ', end='')
    printList(mlist)


if __name__ == '__main__':
    main()
