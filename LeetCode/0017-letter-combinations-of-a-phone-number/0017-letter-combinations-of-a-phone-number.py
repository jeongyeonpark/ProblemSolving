class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        char_map = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}
        
        def backtrack(current_combination, remaining_digits):
            if not remaining_digits:
                result.append(current_combination)
            else:
                for letter in char_map[remaining_digits[0]]:
                    backtrack(current_combination + letter, remaining_digits[1:])

        backtrack('',digits)

        return result