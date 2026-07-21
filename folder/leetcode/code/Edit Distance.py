class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            pre_diag = dp[0]
            dp[0] = i
            w1_char = word1[i - 1] 
            for j in range(1, n + 1):
                temp = dp[j]
                if w1_char == word2[j - 1]:
                    dp[j] = pre_diag
                else:
                    v1 = dp[j]
                    v2 = dp[j - 1] 
                    v3 = pre_diag   
                    if v1 < v2:
                        dp[j] = 1 + (v1 if v1 < v3 else v3)
                    else:
                        dp[j] = 1 + (v2 if v2 < v3 else v3)
                pre_diag = temp
        return dp[n]


                                   (or)



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            pre_diag = dp[0]
            dp[0] = i
            w1_char = word1[i - 1] 
            for j in range(1, n + 1):
                temp = dp[j]
                if w1_char == word2[j - 1]:
                    dp[j] = pre_diag
                else:
                    v1 = dp[j]
                    v2 = dp[j - 1] 
                    v3 = pre_diag   
                    if v1 < v2:
                        dp[j] = 1 + (v1 if v1 < v3 else v3)
                    else:
                        dp[j] = 1 + (v2 if v2 < v3 else v3)
                pre_diag = temp
        return dp[n]
