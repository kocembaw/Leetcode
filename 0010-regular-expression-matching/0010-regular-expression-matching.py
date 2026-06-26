class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] = czy s[i:] pasuje do p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Pusty wzorzec pasuje tylko do pustego stringa
        dp[m][n] = True

        # Iterujemy od końca, bo dp[i][j] zależy od dalszych pozycji
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                # Czy bieżące znaki się zgadzają?
                first_match = i < m and (p[j] == s[i] or p[j] == '.')

                if j + 1 < n and p[j + 1] == '*':
                    # Dwie opcje:
                    # 1) zero wystąpień: pomijamy "znak*" -> dp[i][j+2]
                    # 2) jedno+ wystąpienie: znak pasuje i zostajemy
                    #    przy tym samym wzorcu -> dp[i+1][j]
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # Zwykłe dopasowanie jednego znaku
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]