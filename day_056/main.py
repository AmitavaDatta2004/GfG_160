#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        ans=[]
        n = len(arr)
        
        for i in range(n):
            sum = 0
            k = i
            while sum<target and k<n:
                sum+= arr[k]
                k+=1
            if sum == target:
                ans.append(i+1)
                ans.append(k)
                return ans
                
        ans.append(-1)
        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends