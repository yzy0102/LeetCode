#定义节点
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#将传入的数组转化为链表
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

#传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # n = 0
        # result = head
        # while head:
        #     head = head.next
        #     n += 1
        # for i in range(n // 2):
        #     result = result.next
        # return result
    # 可以使用快慢指针法, 快的走2步, 慢的走1步
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == "__main__":
    head = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    sorted_lists = solution.middleNode(head)
    print(sorted_lists)