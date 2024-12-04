class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        chars = list(s)
        vowels = set('aeiouAEIOU')

        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                chars[l], chars[r] = chars[r], chars[l]
                l, r = l + 1, r - 1
        return ''.join(chars)
        