# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

if __name__ == '__main__':
    S = Solution()
    root = [1,"null",3,2,4,"null",5,6]
    s = S.preorder(root)
    print(s)