class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [None for _ in range(26)]
 
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False

class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
     
      # Returns new trie node (initialized to NULLs)
      return TrieNode()
 
    def _charToIndex(self,ch):
         
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
         
        return ord(ch)-ord('a')
 
    def insert(self,key):
         
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
 
        # mark last node as leaf
        pCrawl.isEndOfWord = True
 
    def search(self, key):
         
        # Search key in the trie
        # Returns true if key presents 
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
 
        return pCrawl.isEndOfWord
    
    def startsWith(self, prefix):
            # Returns true if prefix 
            # presents in trie, else false
            pCrawl = self.root
            length = len(prefix)
            for level in range(length):
                index = self._charToIndex(prefix[level])
                if not pCrawl.children[index]:
                    return False
                pCrawl = pCrawl.children[index]
            return True