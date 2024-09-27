class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        order = {}
        result = []
        for word in strs:
            new_word = ''.join(sorted(list(word)))
            if not new_word in order:
                order[new_word] = len(result)
                result.append([word])
            else:
                result[order[new_word]].append(word)
        return result