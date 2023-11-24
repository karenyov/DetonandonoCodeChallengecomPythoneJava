class Linear:
    def busca (self, nums, target):
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return None

if __name__=="__main__":
    l = Linear()
    print(l.busca([1,3,6,10,12,25],12))