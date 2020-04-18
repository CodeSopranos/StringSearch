import numpy as np
from algorithm.base import Algorithm


class RabinKarp(Algorithm):
    """Rabin-Karp string search algorithm based on hash tables"""

    def __init__(self, reference, hash_function=hash):
        self.reference     = reference
        self.n_operations = 0
        self.hash_function = hash_function

    def get_n_operations(self):
        return self.n_operations
        
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
                self.n_operations += 1
                i = 0
                while self.reference[offset + i] == self.candidate[i]:
                    self.n_operations += 1
                    if (i + 1) == len_candidate:
                        offset_lst.append(offset)
                        if not multiple_search:
                            return offset_lst
                        else:
                            break
                    i += 1
        return offset_lst
