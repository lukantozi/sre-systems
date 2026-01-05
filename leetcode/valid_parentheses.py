class Solution(object):
    def isValid(self, s):
        #s_list = list(s)
        s_list = list(s)
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        for brac_1 in s_list:
            if brac_1 in left:
                brac_ind_left = left.index(brac_1)
                for brac_2 in s_list[1:]:
                    if brac_2 in right:
                        if right.index(brac_2) == brac_ind_left:
                            s_list.remove(brac_1)
                            s_list.remove(brac_2)
                            break
            else:
                return False

        if not s_list:
            return True
        else:
            return False



solution = Solution()
print(solution.isValid("()")) # true
print(solution.isValid("()[]{}")) #true
print(solution.isValid("(]")) # false
print(solution.isValid("([])")) # true
print(solution.isValid("([)]")) # true

