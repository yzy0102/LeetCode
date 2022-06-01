class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        max = 10**3
        min = 10**6
        sum = 0
        for i in salary:
            if i < min:
                min = i
            if i > max:
                max = i
            sum += i
        return float(sum - min - max) / (len(salary) - 2)

if __name__ == '__main__':
    S = Solution()
    salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
    s = S.average(salary)
    print(s)
