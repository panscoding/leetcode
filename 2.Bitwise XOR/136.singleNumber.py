"""
https://leetcode.com/problems/single-number/
"""
import sys

class Sultion:
    def singleNumber(self, nums):
        len_nums = len(nums)
        if len == 1:
            return nums[0]
        ret = nums[0]
        for i in range(1, len_nums):
            ret ^= nums[i]

        return ret

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 4]
    a = Sultion()
    ret = a.singleNumber(nums)
    print(ret)

