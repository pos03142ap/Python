def transform(english_words, start, end):
    potential_ans = [start]
    def recursion():
        tail = potential_ans[-1]
        if potential_ans[-1] == end:
            yield list(potential_ans)
            return
        for w in english_words:
            if is_diff_one(w, tail) and w not in potential_ans:
                potential_ans.append(w)
                yield from recursion()
                potential_ans.pop()
    yield from recursion()

