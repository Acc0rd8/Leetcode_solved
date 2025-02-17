class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        indices = []
        for index in range(len(words)):
            if x in words[index]:
                indices.append(index)
        return indices
    

print(Solution().findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "a"))