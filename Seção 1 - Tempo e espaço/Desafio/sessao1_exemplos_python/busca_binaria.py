from bisect import bisect_left
class Binary:
    def busca (self, nums, target):
        i = bisect_left(nums, target)
        if i != len(nums) and nums[i] == target:
            return i
        return None
if __name__=="__main__":
    l = Binary()
    print(l.busca([1,3,6,10,12,25],12))

