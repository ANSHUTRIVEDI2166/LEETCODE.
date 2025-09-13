class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_vowel = max_consonant = 0
        freq = Counter()
        for c in s:
            freq[c] += 1
            if c in 'aeiou':
                max_vowel = max(max_vowel, freq[c])
            else:
                max_consonant = max(max_consonant, freq[c])
        return max_vowel + max_consonant
