class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        # Helper function for backtracking
        def backtrack(remain: int, combo: list[int], start: int):
            # Base Case 1: Valid combination found
            if remain == 0:
                result.append(list(combo))
                return
            # Base Case 2: Combination sum exceeded target
            elif remain < 0:
                return
            
            # Explore choices
            for i in range(start, len(candidates)):
                # Choose the number
                combo.append(candidates[i])
                # Explore further (pass 'i' to allow reusing the same number)
                backtrack(remain - candidates[i], combo, i)
                # Backtrack (undo the choice)
                combo.pop()
                
        # Start the recursion with full target and index 0
        backtrack(target, [], 0)
        return result

        
