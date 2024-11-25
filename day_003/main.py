class Solution:
    def reverseArray(self, arr):
        left, right = 0, len(arr) - 1
        
        while left < right:
            # Swap elements at left and right pointers
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr