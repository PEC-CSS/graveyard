class Solution:
    def divisibilityArray(self, word: str, m: int):
        n = len(word)
        List = [0] * n
        status = 0
        for i in range(n):
            digit = int(word[i])
            status = (status*10 + digit) % m
            if status == 0:
                List[i] = 1
            else:
                List[i] = 0
        return List