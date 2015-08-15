class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.child = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current = self.root
        for letter in word:
            current.child[letter] = current.child.get(letter, TrieNode())
            current = current.child[letter]
        current.is_end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for letter in word:
            current = current.child.get(letter)
            if current is None:
                return False
        return current.is_end

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current = self.root
        for pre in prefix:
            current = current.child.get(pre)
            if current is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

if __name__ == '__main__':
    trie = Trie()
    trie.insert("somestring")
    print trie.search("key")
    print trie.startsWith("some")