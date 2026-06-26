class Solution:
    def intToRoman(self, num: int) -> str:
        # Pary (wartość, symbol) od największej do najmniejszej,
        # z formami odejmującymi (900, 400, 90, 40, 9, 4) w środku.
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
            (1, "I"),
        ]

        result = []
        for value, symbol in values:
            if num == 0:
                break
            # Ile razy dana wartość mieści się w pozostałej liczbie
            count = num // value
            if count:
                result.append(symbol * count)
                num -= value * count
        return "".join(result)