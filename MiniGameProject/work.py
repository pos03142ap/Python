
def wordladder(fromword, toword, wordset):
    """
    """
self._word_set.add(self._to_word)
        path = []
        path.append((self._from_word, 1))
        temp = path.pop(0)
        tempword = temp[0]
        for i in range(len(self._from_word)):
            char1 = tempword[:i]
            char2 = tempword[i+1:]
            for j in self._chars:
                if tempword[i] != j:
                    new_word = char1 + j + char2
                    if new_word in self._word_set:
                        path.append(new_word)
                        self._word_set.remove(new_word)
        return path