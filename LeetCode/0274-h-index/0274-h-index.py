class Solution:
    def hIndex(self, citations: List[int]) -> int:
        result = []
        max_n = 0
        citations = sorted(citations)

        for i in range(len(citations)):
            if not citations[i] in result:
                result.append(citations[i])

                upper_n = len(citations)-i
                if upper_n >= citations[i] and max_n < citations[i]:
                    max_n = citations[i]
                elif upper_n < citations[i] and max_n < upper_n:
                    max_n = upper_n

        return max_n if max_n != 0 else min(citations[0], len(citations))