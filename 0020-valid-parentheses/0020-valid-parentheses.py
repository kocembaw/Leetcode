class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in pairs:              # nawias zamykający
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:                        # nawias otwierający
                stack.append(ch)
        return not stack