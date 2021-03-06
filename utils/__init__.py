import os


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def nodes_to_list(head):
    l = []
    pt = head
    while pt is not None:
        l.append(pt.val)
        pt = pt.next
    return l


def list_to_nodes(val_list):
    head = ListNode(0)
    pt = head
    for v in val_list:
        n = ListNode(v)
        pt.next = n
        pt = n

    return head.next


def cpath(cf, filename):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(cf)))
    return os.path.join(__location__, filename)
