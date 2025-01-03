class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        if not arr:
            return
        
        n = len(arr)
        
        d = d % n
        
        arr[:] = arr[d:] + arr[:d]