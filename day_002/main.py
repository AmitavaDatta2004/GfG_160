class Solution:
    def pushZerosToEnd(self, arr):
        non_zero_index = 0
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[non_zero_index] = arr[i]
                non_zero_index += 1
        
        while non_zero_index < len(arr):
            arr[non_zero_index] = 0
            non_zero_index += 1
        
        return arr