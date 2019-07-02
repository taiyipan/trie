# Trie class definition
class Trie:
    # TrieNode class definition
    class TrieNode:
        def __init__(self, val = None):
            self._children = dict()
            self._val = val
            self._word = False
    # constructor
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = self.TrieNode()
        self._word_count = 0
        self._char_count = 0
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
            self._build_trie(self._root, letters)
    # insert line
    def insert_line(self, line: str) -> None:
        line = line.strip()
        words = line.split()
        for word in words:
            self.insert(word)
    # recursive function to support insert function
    def _build_trie(self, node: TrieNode, letters: list) -> None:
        if not letters:
            node._word = True
            self._word_count += 1
            return
        letter = letters.pop(0)
        if node._children.get(letter) is None:
            node._children[letter] = self.TrieNode(letter)
            self._char_count += 1
        self._build_trie(node._children[letter], letters)
    # search word
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        letters = list(word)
        return self._word_search(self._root, letters)
    # recursive function to support search function
    def _word_search(self, node: TrieNode, letters: list) -> bool:
        if not letters:
            if node._word:
                return True
            else:
                return False
        letter = letters.pop(0)
        if node._children.get(letter) is None:
            return False
        else:
            return self._word_search(node._children[letter], letters)
    # search for prefix
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        letters = list(prefix)
        return self._prefix_search(self._root, letters)
    # recursive function to support startsWith function
    def _prefix_search(self, node: TrieNode, letters: list) -> bool:
        if not letters:
            return True
        letter = letters.pop(0)
        if node._children.get(letter) is None:
            return False
        else:
            return self._prefix_search(node._children[letter], letters)
    # debug purpose
    def print_trie(self) -> None:
        self._traverse(self._root)
        print('None')
    # recursive function to support debug function
    def _traverse(self, node: TrieNode) -> None:
        print(node._val, '->', end = ' ')
        for key, val in node._children.items():
            self._traverse(val)
    # count how many words in trie
    def count_words(self) -> int:
        return self._word_count
    # count how many chars in trie
    def count_chars(self) -> int:
        return self._char_count


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

trie = Trie()
trie.insert('hello')
trie.insert('world')
trie.insert('hello')
trie.insert_line('         My name, is Taiyi!  ')
trie.print_trie()
print(trie.count_words(), trie.count_chars())
