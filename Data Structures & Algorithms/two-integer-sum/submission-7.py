class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = []
        prevMap = {} # Value : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i] #return array of the index of both values we need, 
            prevMap[n] = i #Since it wasn't found we add to the hashmap and move on
        # for i in range(len(nums)-1):
        #     search = target - nums[i]
        #     if search in nums and nums.index(search) != i:
        #         print("index found: " + str(nums.index(search)))
        #         ind.append(i)
        #         print(ind)
        #         ind.append(nums.index(search,(i+1)))
        #         return ind
        #     continue
        # return ind