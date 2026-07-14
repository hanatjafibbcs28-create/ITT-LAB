import heapq
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # 1. Collect all critical events (left and right edges of buildings)
        events = []
        for left, right, height in buildings:
            # Left edge event: use negative height so sorting prioritizes taller buildings
            events.append((left, -height, right))
            # Right edge event: use 0 as height placeholder to mark ending
            events.append((right, 0, 0))
            
        # 2. Sort events by x-coordinate.
        # Python sorts tuples element by element. If x-coordinates match, 
        # the negative height ensures left edges (tallest first) are processed before right edges.
        events.sort()
        
        # 3. Initialize Max-Heap with a ground level element (height 0, infinity right edge)
        # Python heapq is a min-heap by default, so we store heights as negative numbers.
        max_heap = [(0, float('inf'))] # format: (-height, right_edge)
        
        result = []
        
        # 4. Sweep across all event positions
        for x, neg_h, right in events:
            if neg_h != 0:
                # It's a left edge event! Push it to our active heap
                heapq.heappush(max_heap, (neg_h, right))
            
            # Clean up the heap: remove buildings that have already ended (their right edge <= current x)
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
                
            # Get the current maximum height from the top of the heap
            current_max_height = -max_heap[0][0]
            
            # If the maximum height changed at this x-coordinate, we found a key point!
            if not result or result[-1][1] != current_max_height:
                # To prevent adding duplicate x points, update the height if x is the same
                if result and result[-1][0] == x:
                    result[-1][1] = current_max_height
                else:
                    result.append([x, current_max_height])
                    
        return result

        
