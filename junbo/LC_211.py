class WordDictionary:
    '''
    How to create Tries using _tries = lambda: defaultdict(_tries)
    And how to do backtracking
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        _tries = lambda : defaultdict(_tries)
        self.root = _tries()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            cur = cur[c]
        cur.setdefault('_end')
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(word, i, node):
            if i == len(word):
                return '_end' in node
            elif word[i] == '.':
                return any(
                          helper(word, i+1, node[c])
                          for c in node if c != '_end'
                          )
            elif word[i] in node:
                return helper(word, i+1, node[word[i]])
            else:
                return False
        return helper(word, 0, self.root)
                
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
