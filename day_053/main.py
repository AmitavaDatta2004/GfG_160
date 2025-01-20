#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        ans = []
        start , end = 0 , len(arr) -1
        curClose = float('inf')
        
        while start< end:
            s = arr[start] + arr[end]
            
            if abs(target - s) < curClose:
                curClose = abs(target - s)
                ans = [arr[start] , arr[end]]
                
            if s < target:
                start += 1
            elif s > target:
                end -= 1
            else:
                return [arr[start],arr[end]]
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends