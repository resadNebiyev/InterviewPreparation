class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for z in range(i+1,len(nums)):
                cem = nums[i] + nums[z]
                if cem == target:
                    a = nums.index(nums[i])
                    b = nums.index(nums[z],i+1)
                    return [a,b]
                    