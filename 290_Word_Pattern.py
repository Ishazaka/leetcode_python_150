
// Two hash map

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        charToWord = {}
        wordToChar = {}

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True



// 2nd way


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        charToWord = {}
        wordToChar = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i, (c, word) in enumerate(zip(pattern, words)):
            if charToWord.get(c, 0) != wordToChar.get(word, 0):
                return False
            charToWord[c] = i + 1
            wordToChar[word] = i + 1

        return True



// hash set

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        store = set()
        
        for i, (c, w) in enumerate(zip(pattern, words)):
            if c in charToWord:
                if words[charToWord[c]] != w:
                    return False
            else:
                if w in store:
                    return False
                charToWord[c] = i
                store.add(w)

        return True



// Single Hash Map


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        
        for i, (c, w) in enumerate(zip(pattern, words)):
            if c in charToWord:
                if words[charToWord[c]] != w:
                    return False
            else:
                # iterates atmost 26 times (a - z)
                for k in charToWord:
                    if words[charToWord[k]] == w:
                        return False
                charToWord[c] = i

        return True
