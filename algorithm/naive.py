from algorithm.base import Algorithm


class BruteForce(Algorithm):
    """Naive string search algorithm"""

    def __init__(self, reference):
        self.reference = reference

    @property
    def name(self):
        return 'Brute Force'


    def set_candidate(self, candidate, **params):
        # some preprocessing
        # ...
        self.candidate = candidate


    def search(self, multiple_search=False) -> list:
        offset_lst    = []
        len_reference = len(self.reference)
        len_candidate = len(self.candidate)
        for offset in range(len_reference - len_candidate):
            i = 0
            while self.reference[offset + i] == self.candidate[i]:
                if (i + 1) == len_candidate:
                    offset_lst.append(offset)
                    if not multiple_search:
                        return offset_lst
                    else:
                        break
                i += 1
        return offset_lst
