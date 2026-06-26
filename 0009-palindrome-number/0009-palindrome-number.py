class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Liczby ujemne nie są palindromami (znak minus z przodu).
        # Liczby kończące się na 0 (oprócz samego 0) też nie - bo
        # pierwsza cyfra nie może być 0.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Dla parzystej liczby cyfr: x == reversed_half
        # Dla nieparzystej: środkowa cyfra ląduje w reversed_half,
        # więc pomijamy ją przez x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10