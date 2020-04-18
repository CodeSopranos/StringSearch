import numpy as np
from algorithm.base import Algorithm


class RabinKarp(Algorithm):
    """Rabin-Karp string search algorithm based on hash tables"""

    def __init__(self, reference, hash_function=hash):
        self.reference     = reference
        self.n_operations = 0
        self.hash_function = hash_function
        self.n_operations  = 0


    @property
    def name(self):
        return 'Rabin-Karp'


    def set_candidate(self, candidate, **params):

        self.candidate = candidate
        self.c = 0
        self.r = 0

        self.d = params['d']
        self.q = params['q']
        self.h = (self.d ** (len(candidate) - 1)) % self.q

        result = []
        for i in range(len(candidate)):
            self.c =  self.d * self.c + ord(self.candidate[i])
            self.c %= self.q
            self.r =  self.d * self.r + ord(self.reference[i])
            self.r %= self.q


    def search(self, multiple_search=False)-> list:

        offset_lst = []
        len_ref    = len(self.reference)
        len_can    = len(self.candidate)

        for i in range(len_ref-len_can+1):

           self.n_operations += 1

           if self.c == self.r:
               match = True
               for j in range(len_can):
                   self.n_operations += 1
                   if self.candidate[j] != self.reference[i+j]:
                       match = False
                       break
               if match:
                   offset_lst.append(i)
                   if not multiple_search:
                       return [i]

           if i < len_ref - len_can:
               self.r =  (self.r - self.h * ord(self.reference[i]))
               self.r %= self.q
               self.r =  (self.r * self.d + ord(self.reference[i+len_can]))
               self.r %= self.q
               # self.r =  (self.r + self.q) % self.q

        return offset_lst


    def search_pyhash(self, multiple_search=False) -> list:

        offset_lst     = []
        len_ref  = len(self.reference)
        len_can  = len(self.candidate)
        candidate_hash = self.hash_function(self.candidate)

        for offset in range(int(np.ceil(len_ref / len_can))):
            reference_hash = hash(self.reference[offset:(offset + len_can)])
            if reference_hash == candidate_hash:
                self.n_operations += 1
                i = 0
                while self.reference[offset + i] == self.candidate[i]:
                    self.n_operations += 1
                    if (i + 1) == len_can:
                        offset_lst.append(offset)
                        if not multiple_search:
                            return offset_lst
                        else:
                            break
                    i += 1
        return offset_lst
