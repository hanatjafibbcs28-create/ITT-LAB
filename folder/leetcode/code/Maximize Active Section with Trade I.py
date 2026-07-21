class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        padded_s = '1' + s + '1'
        zero_runs = [len(run) for run in padded_s.split('1') if run]
        if len(zero_runs) < 2:
            return ones
        best = max(zero_runs[i] + zero_runs[i+1] for i in range(len(zero_runs) - 1))
        
        return ones + best


                                         (or)
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")
        padded_s = "1" + s + "1"
        parts = padded_s.split("1")
        zero_runs = []
        inner_ones_runs = []
        current_ones = 0
        for part in parts[1:-1]:
            if part == "":
                current_ones += 1
            else:
                if len(zero_runs) > 0:
                    inner_ones_runs.append(current_ones + 1)
                zero_runs.append(len(part))
                current_ones = 0
        if len(zero_runs) < 2:
            if len(zero_runs) == 1 and padded_s.strip("1") != s:          
                pass
            return ones
        sorted_zeros = sorted(zero_runs, reverse=True)
        max_z1 = sorted_zeros[0]
        max_z2 = sorted_zeros[1]
        best_gain = 0
        for i in range(len(zero_runs) - 1):
            left_z = zero_runs[i]
            right_z = zero_runs[i + 1]
            sacrificed_ones = inner_ones_runs[i]
            gain_A = left_z + right_z
            max_z_elsewhere = max_z2 if (left_z == max_z1 or right_z == max_z1) else max_z1
            gain_B = max_z_elsewhere - sacrificed_ones
            
            best_gain = max(best_gain, gain_A, gain_B)

        return ones + best_gain
