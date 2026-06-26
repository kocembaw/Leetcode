from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Bierzemy pierwszy string jako wzorzec i sprawdzamy
        # kolejne kolumny (znaki) we wszystkich pozostałych.
        for i, ch in enumerate(strs[0]):
            for other in strs[1:]:
                # Jeśli string jest za krótki albo znak się nie zgadza,
                # wspólny prefiks kończy się tuż przed bieżącą pozycją.
                if i >= len(other) or other[i] != ch:
                    return strs[0][:i]
        # Cały pierwszy string jest wspólnym prefiksem.
        return strs[0]