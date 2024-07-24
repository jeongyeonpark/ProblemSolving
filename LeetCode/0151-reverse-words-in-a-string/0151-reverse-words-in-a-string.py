class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        result = []
        for i in range(len(word_list)-1,-1,-1):
            result.append(word_list[i])
        return ' '.join(result)