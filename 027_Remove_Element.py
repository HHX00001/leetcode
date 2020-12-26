给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
class Solution(object):
    # def removeElement(self, nums, val):
    #     ls = len(nums)
    #     if ls == 0:
    #         return ls
    #     pos = 0
    #     for i in range(ls):
    #         if nums[i] == val:
    #             continue
    #         else:
    #             nums[pos] = nums[i]
    #             pos += 1
    #     # del nums[pos:]
    #     return pos

    def removeElement(self, nums, val):
        ls = len(nums)
        if ls == 0:
            return ls
        count = 0
        index = 0
        while index < ls - count:
            if nums[index] == val:
                nums[index] = nums[ls - 1 - count]
                count += 1
            else:
                index += 1
        return ls - count

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.removeElement([1], 1)