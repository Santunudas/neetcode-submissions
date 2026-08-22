class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nn = set()


        for n in nums:
            if n in nn:
                return True
            nn.add(n)
        
        return False