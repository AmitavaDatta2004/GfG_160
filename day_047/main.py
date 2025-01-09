class Solution:
    # Function to return the length of the longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        # Create a set to store unique elements from the array
        num_set = set(arr)
        ans = 0

        for num in arr:
            # Check if it is the start of a sequence
            if num in num_set and (num - 1) not in num_set:
                curr = num
                cnt = 0

                # Count the length of the sequence
                while curr in num_set:
                    num_set.remove(curr)
                    curr += 1
                    cnt += 1

                ans = max(ans, cnt)
        
        return ans
