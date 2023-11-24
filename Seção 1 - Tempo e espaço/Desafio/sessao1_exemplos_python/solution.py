class Solution: 
    def twoSum(self, nums, target):
        dictValues = dict(zip(nums,[x for x in range(len(nums))]))
        for ix,n in enumerate(nums):
            complemento = target - n
            if complemento in dictValues:
                if dictValues[complemento] != ix:
                    return [ix,dictValues[complemento]]
        return None

if __name__=="__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15],9))
    print(solution.twoSum([3,2,4],6))