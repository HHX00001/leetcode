将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

class Solution(object):
    # def convert(self, s, numRows):
    #     """
    #     :type s: str
    #     :type numRows: int
    #     :rtype: str
    #     """
    #     ls = len(s)
    #     if ls <= 1 or numRows == 1:
    #         return s
    #     temp_s = []
    #     for i in range(numRows):
    #         temp_s.append(['']*(ls / 2))
    #     inter = numRows - 1
    #     col, row = 0, 0
    #     for i, ch in enumerate(s):
    #         flag = True
    #         if (i / inter) % 2 == 1:
    #             # print i
    #             flag = False
    #         if flag:
    #             temp_s[row][col] = ch
    #             row += 1
    #         else:
    #             temp_s[row][col] = ch
    #             col += 1
    #             row -= 1
    #     result = ''
    #     for i in range(numRows):
    #         result += ''.join(temp_s[i])
    #     return result

    def convert(self, s, numRows):
        if numRows == 1:
            return s
        # calculate period
        p = 2 * (numRows - 1)
        result = [""] * numRows
        for i in xrange(len(s)):
            floor = i % p
            if floor >= p//2:
                floor = p - floor
            result[floor] += s[i]
        return "".join(result)


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)