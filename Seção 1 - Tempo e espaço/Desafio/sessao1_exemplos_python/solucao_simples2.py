class Solution: 
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complemento = target - nums[i]
            for j in range(len(nums)):
                if complemento == nums[j]:
                    if complemento != nums[i]:
                        return [j, i]
        return None


if __name__=="__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15],9))
    print(solution.twoSum([3,2,4],6))