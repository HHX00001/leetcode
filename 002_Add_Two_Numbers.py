给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     last = 0
    #     head = prev = None
    #     while True:
    #         if l2 is None and l1 is None and last == 0:
    #             break
    #         val = last
    #         if l2 is not None:
    #             val += l2.val
    #             l2 = l2.next
    #         if l1 is not None:
    #             val += l1.val
    #             l1 = l1.next
    #         if val >= 10:
    #             val = val % 10
    #             last = 1
    #         else:
    #             last = 0
    #         current = ListNode(val)
    #         if prev is None:
    #             head = current
    #         else:
    #             prev.next = current
    #         prev = current
    #     return head

    def addTwoNumbers(self, l1, l2):
        carry = 0
        # dummy head
        head = curr = ListNode(0)
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = val / 10
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next