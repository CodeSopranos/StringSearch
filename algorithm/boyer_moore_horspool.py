from collections import defaultdict
from algorithm.base import Algorithm
from string import ascii_letters


class BoyerMooreHorspool(Algorithm):

    def __init__(self, reference):
 #       reference = reference.translate(reference.maketrans('', '', ascii_letters))
        self.reference = reference
        self.n_operations = 0


    @property
    def name(self):
        return 'Boyer-Moore-Horspool'

    def set_candidate(self, candidate, **params):
        self.candidate = candidate

    def set_skip_table(self):
        len_ref = len(self.reference)
        len_can = len(self.candidate)
        if len_can > len_ref:
            print("Error: len candidate > len references {} > {}." \
                              .format(len_can, len_ref))
            return -1

        self.table_skip = defaultdict(lambda: len_can)

        for offset in range(len_can - 1):
            self.table_skip[ord(self.candidate[offset])] = len_can - offset - 1

    def search(self, multiple_search=False) -> list:
        self.set_skip_table()

        len_ref = len(self.reference)
        len_can = len(self.candidate)

        offset_lst = []
        offset = len_can - 1

        while offset < len_ref:
            j = len_can - 1
            i = offset
            self.n_operations += 1
            while j >= 0 and self.reference[i] == self.candidate[j]:
                self.n_operations += 1
                j -= 1
                i -= 1
            if j == -1:
                offset_lst.append(i + 1)
            offset += self.table_skip[ord(self.reference[offset])]

        return offset_lst
