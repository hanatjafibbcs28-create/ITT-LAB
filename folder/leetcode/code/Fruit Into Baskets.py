class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_fruits = curr_len = last_streak = 0
        t1 = t2 = -1
        for f in fruits:
            curr_len = curr_len + 1 if f in (t1, t2) else last_streak + 1
            last_streak = last_streak + 1 if f == t2 else 1
            if f != t2: t1, t2 = t2, f
            if curr_len > max_fruits: max_fruits = curr_len
        return max_fruits
