"""
1009
https://leetcode.com/problems/complement-of-base-10-integer/
"""

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        """
        1. Solution:
        XOR property: 1^0 = 1, 1^1 = 0, 0^0 = 0
        From the property of XOR, we can conclude that XOR of a number with its complement will result in a number
        that has all of its bits set to 1. i.e., 1000 ^ 0111 = 1111
        complement = all_set_bit ^ N
        all_set_bit = pow(2, count_bit) - 1 i.e.,  N = 1000, count_bit = 4, complement = pow(2, 4) - 1
        2. Time Complexity:
        The time complexity of this solution is O(n) where n is the number of bits required to store the given number.
        3. Space Complexity
        The solution runs in constant space O(1)
        :param N:
        :return:
        """
        if N == 0:
            return 1
        #1.count the number of bit for input N
        count_bit = 0
        num = N
        while N > 0:
            count_bit +=1
            N = N >> 1
        # print("count_bit:", count_bit)

        #2. get the all set bit number = 2^count_bit - 1
        all_set_bit = pow(2, count_bit) - 1
        # print("all_set_bit: ", all_set_bit)

        #3. complement = N xor all_set_bit
        return num ^ all_set_bit


def main():
    N = 8
    a = Solution()
    ret = a.bitwiseComplement(N)
    print("ret: ", ret)

if __name__ == "__main__":
    main()