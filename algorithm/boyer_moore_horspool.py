from collections import defaultdict
from algorithm.base import Algorithm
from string import ascii_letters


class BoyerMooreHorspool(Algorithm):

    def __init__(self, reference):
        self.n_operations = 0
 #       reference = reference.translate(reference.maketrans('', '', ascii_letters))
        self.reference = reference

    def get_n_operations(self):
        return self.n_operations
    
    @property
    def name(self):
        return 'Boyer-Moore-Horspool'

    def set_candidate(self, candidate, **params):
        self.candidate = candidate

    def set_skip_table(self):
        len_reference = len(self.reference)
        len_candidate = len(self.candidate)
        if len_candidate > len_reference:
            print("Error: len candidate > len references {} > {}.".format(len_candidate, len_reference))
            return -1

        self.table_skip = defaultdict(lambda: len_candidate) 

        for offset in range(len_candidate - 1):
            self.table_skip[ord(self.candidate[offset])] = len_candidate - offset - 1
        
    def search(self, multiple_search=False) -> list:
        self.set_skip_table()

        len_reference = len(self.reference)
        len_candidate = len(self.candidate)

        offset_lst = []
        offset = len_candidate - 1

        while offset < len_reference:
            j = len_candidate - 1
            i = offset
            while j >= 0 and self.reference[i] == self.candidate[j]:
                self.n_operations += 1
                j -= 1
                i -= 1
            if j == -1:
                offset_lst.append(i + 1)
            offset += self.table_skip[ord(self.reference[offset])]

        return offset_lst
