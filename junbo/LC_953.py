class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''1) first solution''''
        # generate HashTable 
        T = {c:i for i, c in enumerate(order)}
        # start checking
        # at first I compare all char i for all words, making problem
        # very hard
        # need to think how we compare list of digits in reality
        # for else structure is needed 
        for earlier, later in zip(words, words[1:]):
            for i in range(min(len(earlier), len(later))):
                if earlier[i] != later[i]:
                    if T[earlier[i]] < T[later[i]]:
                        break
                    return False
            else:
                if len(earlier) > len(later):
                    return False
        return True
        '''
        2) second solution,
        leverage python can compare list of int
        leverage python  can automatically compare list of
           digits lexicographically
        '''
        # generate HashTable
        T = {c:i for i, c in enumerate(order)}
        # convert each word to a list of int
        words = [[T[c] for c in word] for word in words]
        # compare every two pairs make make sure the left word1 <= right word2
        return all(word1 < word2 for word1, word2 in zip(words, words[1:]))
        
            
