"""
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.

Example 1:

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]

"""

class Solution:
    def twoSingleNumber(self, nums) -> list:
        """
        1.Solution
        If we XOR all the numbers in the input array. The same number will be cancel each other. The final result is
        n1^n2 where n1 is one of missing number, n2 is other missing number. As we know those two number must have one bit different.
        The idea is use this one bit different to partition all the numbers to two group. one group this bit position will be 0,
        other group this bit will be 1. The input array will be partition two group one group including the missing number one.
        another group will include the missing number two. For each sub-group we will do the XOR for all numbers. Ther result will be
        the missing number one and number two

        2. Time Complexity
        The time complexity of this solution is O(n) where n is the number of elements in the input array.

        3. Space Complexity
        The Solution runs in constant space O(1)
        :param arr:
        :return:
        """
        #1. get the XOR result of missing number n1 ^ missing number n2
        n1_n2 = 0
        for num in nums:
            n1_n2 ^= num

        #2 find the different postion between n1 and n2 (equeal to 1)
        position = 1
        while (position & n1_n2) == 0:
            position = position << 1
        num1, num2 = 0, 0

        #3.divid the nums to tow group. one group the bit poistion equal to 0, another group the bit position equal to 1
        for num in nums:
            if (position & num) == 0:
                num1 ^= num #XOR each group
            else:
                num2 ^= num #XOR each group

        return [num1, num2]


def main():
    nums = [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
    a = Solution()
    ret = a.twoSingleNumber(nums)
    print(ret)


if __name__ == "__main__":
    main()