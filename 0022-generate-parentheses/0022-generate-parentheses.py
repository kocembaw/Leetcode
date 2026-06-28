from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            # Mamy kompletną kombinację: użyliśmy n par
            if len(current) == 2 * n:
                result.append(current)
                return

            # Możemy dodać '(' dopóki nie przekroczyliśmy n nawiasów otwierających
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Możemy dodać ')' tylko jeśli jest niezamknięty nawias otwierający
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result