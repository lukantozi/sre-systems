class Solution(object):
    def isValid(self, s):
        s_list = list(s)
        #--------0,   1,   2
        left = ["(", "[", "{"]
        right = [")", "]", "}"]

        flag = True
        while flag:
            curr_ptr = 0
            next_ptr = 1
            if s_list == []:
                return True
            current_bracket = s_list[curr_ptr]
            if current_bracket in right:
                return False
            # if in left
            flag_inner = True
            while flag_inner:
                current_bracket = s_list[curr_ptr]
                left_index = left.index(current_bracket)
                try:
                    next_bracket = s_list[next_ptr]
                except IndexError:
                    return False
                if next_bracket in right:
                    if left_index == right.index(next_bracket):
                        s_list.pop(curr_ptr)
                        s_list.pop(next_ptr-1)
                        curr_ptr = curr_ptr - 1 if curr_ptr > 0 else 0
                        next_ptr = curr_ptr + 1
                        flag_inner = False
                        continue
                    else:
                        return False
                else:
                    curr_ptr += 1
                    next_ptr += 1

        

solution = Solution()
print(solution.isValid("()")) # true
print(solution.isValid("()[]{}")) #true
print(solution.isValid("(]")) # false
print(solution.isValid("([])")) # true
print(solution.isValid("([)]")) # false
print(solution.isValid("[([]])")) # false
