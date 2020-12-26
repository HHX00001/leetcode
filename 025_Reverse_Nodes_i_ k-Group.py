给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def reverseKGroup(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None:
            return None
        index = 0
        lead, last = 0, 0
        pos = head
        temp = ListNode(-1)
        temp.next = head
        head = temp
        start = head
        while pos is not None:
            if index % k == k - 1:
                last = pos.next
                start = self.reverseList(start, last)
                pos = start
            pos = pos.next
            index += 1
        return head.next

    def reverseList(self, head, end):
        pos = head.next
        last = end
        next_start = pos
        while pos != end:
            head.next = pos
            last_pos = pos
            pos = pos.next
            last_pos.next = last
            last = last_pos
        return next_start