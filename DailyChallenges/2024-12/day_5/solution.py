class Solution(object):
    def canChange(self, start, target):
        start_positions = start.replace('_', '')
        target_positions = target.replace('_', '')

        if start_positions != target_positions:
            return False

        start_L_index = [i for i, c in enumerate(start) if c == 'L']
        target_L_index = [i for i, c in enumerate(target) if c == 'L']

        for i, j in zip(start_L_index, target_L_index):
            if i < j:
                return False

        start_R_index = [i for i, c in enumerate(start) if c == 'R']
        target_R_index = [i for i, c in enumerate(target) if c == 'R']

        for i, j in zip(start_R_index, target_R_index):
            if i > j:
                return False
        return True