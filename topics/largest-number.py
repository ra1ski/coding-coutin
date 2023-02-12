class LargerNumKey(str):
    def __lt__(x, y):
        a = x + y
        b = y + x
        r = a > b
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

s = Solution()
r = s.largestNumber([3,30,34,5,9])
...