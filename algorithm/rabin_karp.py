import numpy as np
from algorithm.base import Algorithm


class RabinKarp(Algorithm):
    """Rabin-Karp string search algorithm based on hash tables"""

    def __init__(self, reference, hash_function=hash):
        self.reference     = reference
        self.hash_function = hash_function


    @property
    def name(self):
        return 'Rabin-Karp'


    def set_candidate(self, candidate, **params):
        self.candidate = candidate


    def search(self, multiple_search=False) -> list:

        offset_lst     = []
        len_reference  = len(self.reference)
        len_candidate  = len(self.candidate)
        candidate_hash = self.hash_function(self.candidate)

        for offset in range(int(np.ceil(len_reference / len_candidate))):
            reference_hash = hash(self.reference[offset:(offset + len_candidate)])
            if reference_hash == candidate_hash:
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
