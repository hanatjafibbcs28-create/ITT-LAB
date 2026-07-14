class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # 1. Return early if the input list is empty
        if not intervals:
            return []
        
        # 2. Sort the intervals based on their start times
        intervals.sort(key=lambda x: x[0])
        
        # 3. Initialize the merged list with the first interval
        merged = [intervals[0]]
        
        # 4. Iterate through the remaining intervals
        for current in intervals[1:]:
            last_merged = merged[-1]
            
            # If current start time is less than or equal to last merged end time, they overlap
            if current[0] <= last_merged[1]:
                # Update the end time of the last merged interval to the larger end time
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, so append the current interval as a new entry
                merged.append(current)
                
        return merged
