给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #     ls = len(nums)
    #     if ls <= 1:
    #         return ls
    #     last = nums[0]
    #     pos = 1
    #     for t in nums[1:]:
    #         if t == last:
    #             continue
    #         else:
    #             nums[pos] = t
    #             pos += 1
    #             last = t
    #     return pos

    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == nums[i]:
                continue
            else:
                left += 1
                nums[left] = nums[i]
        return left + 1
