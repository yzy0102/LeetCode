class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        """ 方法1 遍历"""
        # right = 0
        # new_commd = ""
        # n = len(command)
        # while right < n:
        #     if command[right] == "G":
        #         right += 1
        #         new_commd += "G"
        #     else:
        #         right += 1
        #         if command[right] == ")":
        #             new_commd += "o"
        #             right += 1
        #         else:
        #             new_commd += "al"
        #             right += 3
        # return new_commd
        """方法2: 直接替换"""
        return command.replace('()', 'o').replace('(al)', 'al')


if __name__ == '__main__':
    S = Solution()
    command = "GG()"
    s = S.interpret(command)
    print(s)