class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)

        for i in range (n * 2):
            if i < n:
                output.append(nums[i])
            else:
                output.append(nums[i - n])
        return output