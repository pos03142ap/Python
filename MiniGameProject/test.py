__author__ = 'pos03142ap'

def extensions(self, next_word):
        """
        Extensions of WordLadderPuzzle that solves the Puzzle.

        Precondition: Words has to be same length

        >>> ws1 = ["cast", "case", "cave"]
        >>> wl1 = WordLadderPuzzle("cost", "save", ws1)
        >>> wl1.extensions
        []
        """
        if len(self._from_word) != len(next_word)
            raise ("Words must be equal lenth")
        else:
            for i,j in range(len(self._from_word)), self._chars:
                if self._from_word != j:
                    nextword =



        path = []
        path.append(self._from_word)
        for i in range(len()):
            chars = path[-1]
            chars1 = chars[:i]
            chars2 = chars[i+1:]
            for j in self._chars:
                if chars[i] != j:
                    new_word = chars1 + j + chars2
                    path.append(new_word)
                    self._from_word = new_word
        if path[-1] == self._to_word:
            self.word_ladder.append(path)
        return path