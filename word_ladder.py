class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList) ## O(1) lookup
        
        if endWord not in words:
            return 0
        
        q = deque([(beginWord, 1)])
        
        while q:
            
            word , length = q.popleft()
            
            if word ==  endWord:
                return length
            
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz' :
                    next_word = word[:i] + char+word[i+1:]
                    
                    if next_word in words:
                        words.remove(next_word)
                        q.append((next_word,length+1))
                
        
        
        
        
        
        
        
        return 0
        
