class Solution:
    def romanToInt(self, s: str) -> int:
        # Słownik mapujący symbole rzymskie na wartości całkowite
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # Pobieramy wartość bieżącego symbolu
            current_val = roman_map[s[i]]
            
            # Jeśli nie jesteśmy na ostatnim znaku i bieżący symbol
            # jest mniejszy niż kolejny, odejmujemy go (np. IV, XC)
            if i < n - 1 and current_val < roman_map[s[i + 1]]:
                total -= current_val
            else:
                total += current_val
                
        return total

# --- Przykład użycia ---
sol = Solution()
print(sol.romanToInt("III"))      # Wyjdzie: 3
print(sol.romanToInt("LVIII"))    # Wyjdzie: 58
print(sol.romanToInt("MCMXCIV"))  # Wyjdzie: 1994