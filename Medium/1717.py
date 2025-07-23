class Solution(object):
    def maximumGain(self, s, x, y):
        stack_main = []
        total_score = 0

        # Decide which substring to prioritize based on higher value
        if x > y:
            primary_pair = ["a", "b"]
            primary_score = x
            secondary_pair = ["b", "a"]
            secondary_score = y
        else:
            primary_pair = ["b", "a"]
            primary_score = y
            secondary_pair = ["a", "b"]
            secondary_score = x

        # First pass: Remove all instances of the primary pair
        for ch in s:
            stack_main.append(ch)
            if stack_main[-2:] == primary_pair:
                stack_main.pop()
                stack_main.pop()
                total_score += primary_score

        # Second pass: Remove all instances of the secondary pair
        stack_final = []
        for ch in stack_main:
            stack_final.append(ch)
            if stack_final[-2:] == secondary_pair:
                stack_final.pop()
                stack_final.pop()
                total_score += secondary_score

        return total_score
