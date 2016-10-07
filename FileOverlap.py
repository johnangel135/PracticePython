def overlap():
    def slurp(A):
        with open(A) as x:
            return map(lambda x: int(x), x.readlines())

    def get_overlap(A, B):
        sA = set(slurp(A))
        return [e for e in slurp(B) if e in sA]

    overlap = get_overlap('primenumbers.txt', 'happynumbers.txt')
    return overlap