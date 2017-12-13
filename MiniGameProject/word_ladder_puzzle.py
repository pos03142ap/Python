from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"
        self.correct_path = []

    def __eq__(self, other):
        """
        Return whether WordLadderPuzzle self is equivalent to other

        @param Shape Word
        @rtype: bool

        >>> ws1 = ["lama", "lana", "lang"]
        >>> wl1 = WordLadderPuzzle("lamb", "hang", ws1)
        >>> wl2 = WordLadderPuzzle("lamb", "hang", ws1)
        >>> wl1 == wl2
        True
        >>> ws2 = ["lam", "lag"]
        >>> wl3 = WordLadderPuzzle ("ham", "log", ws2)
        >>> wl1 == wl3
        False
        """
        return (type(self) == type(other) and
                (self._from_word, self._to_word) == (other._from_word, other._to_word) and
                self._word_set  == other._word_set)

    def extensions(self):
        """
        Extensions of WordLadderPuzzle that solves the Puzzle.

        Precondition: Words has to be same length
        @rtype: list

        >>> ws1 = ["cast", "case", "cave"]
        >>> wl1 = WordLadderPuzzle("cost", "save", ws1)
        >>> wl1.extensions()
        >>> ws1 = ["case", "cave"]
        """
        self._word_set.append(self._to_word)
        path = [self._from_word]
        for i in range(len(self._from_word)):
            char1 = self._from_word[:i]
            char2 = self._from_word[i+1:]
            for j in self._chars:
                if self._from_word[i] != j:
                    new_word = char1 + j + char2
                    if new_word in self._word_set:
                        path.append(new_word)
                        self.correct_path.append(path)
                        self._word_set.remove(new_word)
                    elif new_word == self._to_word:
                        path.append(self._to_word)

        return None

    def __str__(self):
        """
        Return a user-friendly string representation of the word ladder
        @rtype: str

        >>> ws1 = ["cast", "case", "cave"]
        >>> wlp1 = WordLadderPuzzle("cost", "save", ws1)
        >>> wlp1.extensions()
        >>> print(wlp1)
        'cost -> cast -> case -> cave -> save'
        """
        return (' -> '.join(self.extensions().path))

    def is_solved(self):
        """
        this WordLadderPuzzle is solved when _from_word is the same as _to_word

        >>> wlp1 = WordLadderPuzzle("cost", "save". ws1)
        >>> wlp1.is_solved
        False
        >>> wlp1 = WordLadderPuzzle("save", "save", ws1)
        >>> wlp1.is_solved
        True
        """
        return self._from_word == self._to_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
