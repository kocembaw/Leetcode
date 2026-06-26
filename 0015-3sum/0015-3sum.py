from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Pomijamy duplikaty pierwszego elementu, by nie powielać trójek.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Skoro tablica jest posortowana, jeśli najmniejszy element
            # jest dodatni, suma trzech będzie dodatnia - koniec.
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1          # za mało - zwiększamy sumę
                elif total > 0:
                    right -= 1         # za dużo - zmniejszamy sumę
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Pomijamy duplikaty obu wskaźników po znalezieniu trójki.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result