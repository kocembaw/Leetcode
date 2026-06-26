from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Wysokość ogranicza niższa z dwóch linii,
            # szerokość to odległość między wskaźnikami.
            h = min(height[left], height[right])
            width = right - left
            max_water = max(max_water, h * width)

            # Przesuwamy wskaźnik od niższej linii - to jedyny ruch,
            # który daje szansę na większe pole.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water