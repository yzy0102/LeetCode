# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ans = 0
        # 每读到下一个数, 把前一个数按位左移就可以不用事先知道链表长度
        # i << n 相当于把i乘以2的n次方；i >> n相当于i除以2的i次方
        while head:
            ans = (ans<<1) + head.val
            head = head.next
        return ans
if __name__ == '__main__':
    S = Solution()
    head = [1,0,1]
    s = S.getDecimalValue(head)
    print(s)
