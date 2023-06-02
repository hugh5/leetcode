"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a
dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie
boolean startsWith(String prefix) Returns true if there is a previously inserted string that has the prefix "prefix"
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}


class Trie:

    def __init__(self):
        self.start = Node("")

    def insert(self, word: str) -> None:
        curr = self.start
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                n = Node(c)
                curr.children[c] = n
                curr = n
        curr.children[""] = Node("")

    def search(self, word: str) -> bool:
        curr = self.start
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return "" in curr.children

    def startsWith(self, prefix: str) -> bool:
        curr = self.start
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert("hugh")
    print(t.search("hugh"))
    print(t.search("hug"))
    print(t.search("hughd"))
    print(t.startsWith("hug"))
    print(t.startsWith("hughd"))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
