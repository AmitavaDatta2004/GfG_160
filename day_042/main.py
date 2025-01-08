class Solution:
	def twoSum(self, arr, target):
		# code here
		seen = set()
		for num in arr :
			if target - num in seen:
				return True
			seen.add(num)
		return False