class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, name):
        node = self.root
        for char in name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def find(self, partial):
        node = self.root
        for char in partial:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

def contacts(queries):
    trie = Trie()
    results = []

    for query in queries:
        operation, value = query
        if operation == "add":
            trie.add(value)
        elif operation == "find":
            results.append(trie.find(value))

    return results

if __name__ == '__main__':
    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    for res in result:
        print(res)
