class Solution(object):
    def isValid(self, s):
        want = {'(' : ')', '[' : ']', '{' : '}'}
        st = []
        for ch in s:
            if ch in want:
                st.append(want[ch])          # push what we expect next
            else:
                if not st or st.pop() != ch: # mismatch or premature close
                    return False
        return not st
