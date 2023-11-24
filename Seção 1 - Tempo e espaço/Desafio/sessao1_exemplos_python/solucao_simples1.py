class Solution: 
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complemento = target - nums[i]
            if complemento in nums:
                if complemento != nums[i]:
                    return [nums.index(complemento), i]
        return None


if __name__=="__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15],9))
    print(solution.twoSum([3,2,4],6))