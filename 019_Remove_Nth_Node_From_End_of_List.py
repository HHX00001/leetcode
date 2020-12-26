给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

class Solution(object):
    # def removeNthFromEnd(self, head, n):
    #     # with O(n) space
    #     index = []
    #     pos = head
    #     while pos is not None:
    #         index.append(pos)
    #         pos = pos.next
    #     ls = len(index)
    #     if n == ls:
    #         if ls > 1:
    #             return index[1]
    #         else:
    #             return None
    #     else:
    #         index_pos = ls - n - 1
    #         index[index_pos].next = index[index_pos + 1].next
    #         return head

    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        slow = fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            head = head.next
            return head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        curr = slow.next
        slow.next = curr.next
        return head