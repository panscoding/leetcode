"""

"""
def longest_substring_with_k_distinct(str1, K):
    window_start = 0
    max_length = 0
    char_frequency = {}

    #for loop the str
    for window_end in range(len(str1)):
        #1. get current char
        current_char = str1[window_end]

        #2 add current char to char frequency
        if current_char not in char_frequency:
            char_frequency[current_char] = 0
        char_frequency[current_char] += 1

        #3. shrink the sliding window until we are left with k distinc charcters in the char_frequency
        while len(char_frequency) > K:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1 #shrink the window
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()