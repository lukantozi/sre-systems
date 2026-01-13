class Solution:
    def characterReplacement(self, s: str, k: int):
        if k >= len(s)-1:
            return len(s)

        def longest(s):
            l, r = 0, 1
            len_s = len(s)
            max_len = 1
            ind_l = 0
            ind_r = 0
            while r < len_s:
                if s[l] == s[r]:
                    r += 1
                    max_len = max(max_len, r - l)
                    ind_l = l
                    ind_r = r-1
                else:
                    l = r
                    r = l + 1
            return max_len, ind_l , ind_r

        if k == 0:
            consec_ls, _, _ = longest(s)
            return consec_ls

        s_size = len(s)
        s_lis = list(s)
        consec_ls, l, r = longest(s_lis)
        while k > 0:
            if l-1 > 0:
                s_lis[l-1] = s_lis[l]
                consec_ls, l, r = longest(s_lis)
                k -= 1
            elif r < s_size-1:
                s_lis[r+1] = s_lis[r]
                consec_ls, l, r = longest(s_lis)
                k -= 1
            else:
                return s_size
        #return s_lis, consec_ls, l, r
        return consec_ls


print(Solution().characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4))
#print(Solution().characterReplacement("ABAB", 2))
#print(Solution().characterReplacement("AABABBA", 1))
#print(Solution().characterReplacement("AAAA", 2))
#print(Solution().characterReplacement("ABBABBAAA", 1))
#print(Solution().characterReplacement("ABABBBBAAA", 1))
