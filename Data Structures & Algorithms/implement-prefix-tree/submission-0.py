class TreeNode: 
    def __init__(self):
        self.c = -1
        self.children = []
        self.endOfWord = False
    

class PrefixTree:

    def __init__(self):
        self.tree = TreeNode()

    def insert(self, word: str) -> None:
        if str is None:
            return 
        
        current = self.tree
        for i,c in enumerate(word):
            valOfChar = ord(c) - ord('a')
            found = None

            for child in current.children:
                if child.c == valOfChar:
                    found = child
                    break
            
            if not found:
                node = TreeNode()
                node.c = valOfChar
                current.children.append(node)
                current = node
            else:
                current = found
            
        current.endOfWord = True

    def search(self, word: str) -> bool:
        if word is None:
            return True
        
        curr = self.tree
        for i,c in enumerate(word):
            valOfChar = ord(c) - ord('a')
            isFound = False

            for child in curr.children:
                if child.c == valOfChar:
                    isFound = True
                    curr = child
                    break
            
            if not isFound:
                return False
            
            if i == len(word) - 1 and not curr.endOfWord:
                return False
            
        return True

    def startsWith(self, prefix: str) -> bool:
        if prefix is None:
            return True
        
        curr = self.tree
        for i,c in enumerate(prefix):
            valOfChar = ord(c) - ord('a')
            isFound = False

            for child in curr.children:
                if child.c == valOfChar:
                    curr = child
                    isFound = True
                    break
            
            if not isFound:
                return False
            
        return True

        
        