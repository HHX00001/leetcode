给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
class Solution(object):
    # def swapPairs(self, head):
    #     current = last = last2 = head
    #     while current is not None:
    #         nex = current.next
    #         if current == last.next:
    #             last.next = nex
    #             current.next = last
    #             if last == head:
    #                 head = current
    #             else:
    #                 last2.next = current
    #             last2 = last
    #             last = nex
    #         current = nex
    #     return head

    def swapPairs(self, head):
        dummyHead = ListNode(-1)
        dummyHead.next = head
        prev, p = dummyHead, head
        while p != None and p.next != None:
            q, r = p.next, p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummyHead.next