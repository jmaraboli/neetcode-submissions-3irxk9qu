class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            i_count = nums.count(i)
            if i_count > 1:
                return True
            continue
        return False

        