给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。


# class Solution(object):
#     def isValid(self, s):
        
#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        stack = []
        for t in s:
            if t == ')':
                try:
                    current = stack.pop()
                    if current != '(':
                        return False
                except:
                    return False
            elif t == '}':
                try:
                    current = stack.pop()
                    if current != '{':
                        return False
                except:
                    return False
            elif t == ']':
                try:
                    current = stack.pop()
                    if current != '[':
                        return False
                except:
                    return False
            else:
                stack.append(t)
        if len(stack) == 0:
            return True
        else:
            return False


    # def isValid(self, s):
    #     # python replace
    #     n = len(s)
    #     if n == 0:
    #         return True
    #
    #     if n % 2 != 0:
    #         return False
    #
    #     while '()' in s or '{}' in s or '[]' in s:
    #         s = s.replace('{}', '').replace('()', '').replace('[]', '')
    #
    #     if s == '':
    #         return True
    #     else:
    #         return False