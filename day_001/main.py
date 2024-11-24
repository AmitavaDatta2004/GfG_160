class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
        
        largest = second_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                largest = num
        
        for num in arr:
            if num > second_largest and num < largest:
                second_largest = num
        
        return second_largest if second_largest != float('-inf') else -1