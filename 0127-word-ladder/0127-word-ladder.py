class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        dict = defaultdict(list)
        # n x m
        for word in wordList:
            for i in range(0, n):
                dict[word[:i] + "-" + word[i+1:]].append(word)
                # h-t -ot and etc
        level = 0
        queue = collections.deque([[beginWord, 1]])
        visited = set()
        visited.add(beginWord)
        # n x m x n -> Time complexity 
        while queue:
            interm_word, level = queue.popleft()
            # n
            for i in range(0, n):
                processed_word = interm_word[:i] + '-' + interm_word[i+1:]
                for word in dict[processed_word]:
                        if word == endWord:
                            return level + 1
                        if word not in visited:
                            visited.add(word)
                            queue.append((word, level + 1))
        return 0
