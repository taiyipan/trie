# Trie class definition
class Trie:
    # TrieNode class definition
    class TrieNode:
        def __init__(self, val = None):
            self.children = dict()
            self.val = val
            self.word = False
    # constructor
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()
        self.word_count = 0
        self.char_count = 0
    # insert word
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        import string
        word = word.lower()
        trans = str.maketrans('', '', string.punctuation)
        word = word.translate(trans)
        if not self.search(word):
            letters = list(word)
            self.build_trie(self.root, letters)
    # insert line
    def insert_line(self, line: str) -> None:
        line = line.strip()
        words = line.split()
        for word in words:
            self.insert(word)
    # recursive function to support insert function
    def build_trie(self, node: TrieNode, letters: list) -> None:
        if not letters:
            node.word = True
            self.word_count += 1
            return
        letter = letters.pop(0)
        if node.children.get(letter) is None:
            node.children[letter] = self.TrieNode(letter)
            self.char_count += 1
        self.build_trie(node.children[letter], letters)
    # search word
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        letters = list(word)
        return self.word_search(self.root, letters)
    # recursive function to support search function
    def word_search(self, node: TrieNode, letters: list) -> bool:
        if not letters:
            if node.word:
                return True
            else:
                return False
        letter = letters.pop(0)
        if node.children.get(letter) is None:
            return False
        else:
            return self.word_search(node.children[letter], letters)
    # search for prefix
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        letters = list(prefix)
        return self.prefix_search(self.root, letters)
    # recursive function to support startsWith function
    def prefix_search(self, node: TrieNode, letters: list) -> bool:
        if not letters:
            return True
        letter = letters.pop(0)
        if node.children.get(letter) is None:
            return False
        else:
            return self.prefix_search(node.children[letter], letters)
    # debug purpose
    def print_trie(self) -> None:
        self.traverse(self.root)
        print('None')
    # recursive function to support debug function
    def traverse(self, node: TrieNode) -> None:
        print(node.val, '->', end = ' ')
        for key, val in node.children.items():
            self.traverse(val)
    # count how many words in trie
    def count_words(self) -> int:
        return self.word_count
    # count how many chars in trie
    def count_chars(self) -> int:
        return self.char_count


# trie = Trie()
# trie.insert('apple')
# print('Search apple:', trie.search('apple')) # True
# print('Search app:', trie.search('app')) # False
# print('Prefix app:', trie.startsWith('app')) # True
# trie.insert('app')
# print('Search app:', trie.search('app')) # True
#
# trie.print_trie()
# print('Words: {}'.format(trie.count_words()))
# print('Characters: {}'.format(trie.count_chars()))

# trie = Trie()
# trie.insert('hello')
# trie.insert('world')
# trie.insert('hello')
# trie.insert_line('         My name, is Taiyi!  ')
# trie.print_trie()
# print(trie.count_words(), trie.count_chars())
