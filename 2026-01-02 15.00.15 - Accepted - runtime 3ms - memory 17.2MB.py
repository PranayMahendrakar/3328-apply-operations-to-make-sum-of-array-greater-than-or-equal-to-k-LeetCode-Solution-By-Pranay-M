class Solution:
    def minOperations(self, k: int) -> int:
        if k <= 1:
            return 0
        
        # We start with [1], can increment or duplicate
        # If we increment to v, then duplicate d times: sum = (d+1)*v
        # Operations = (v-1) + d
        # Want min (v-1) + d such that (d+1)*v >= k
        
        result = float('inf')
        
        # Try each possible final value v
        for v in range(1, k + 1):
            # Need (d+1) * v >= k, so d >= ceil(k/v) - 1
            d = (k + v - 1) // v - 1  # This is ceil(k/v) - 1
            d = max(0, d)
            ops = (v - 1) + d
            result = min(result, ops)
            
            # Optimization: once ops starts increasing, we can stop
            if v - 1 > result:
                break
        
        return result