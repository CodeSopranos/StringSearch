from collections import defaultdict
from algorithm.base import Algorithm
from string import ascii_letters


class KnuthMorrisPratt(Algorithm):

    def __init__(self, reference):
        # reference = reference.translate(reference.maketrans('', '', ascii_letters))
        self.reference = reference
        self.n_operations = 0


    @property
    def name(self):
        return 'Knuth-Morris-Pratt'

    def set_candidate(self, candidate, **params):
        self.candidate = candidate

    def search(self, multiple_search=False) -> list:
        """Return the lowest index of T at which substring P begins (or else -1)."""
        len_ref = len(self.reference)
        len_can = len(self.candidate)

        if len_can > len_ref:
            print("Error: len candidate > len references {} > {}.".format(len_can, len_ref))
            return -1
        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        self.lps = [0] * len_can
        j = 0  # index for pat[]

        # Preprocess the pattern
        self.computeLPSArray()
        offset_lst = []

        i = 0  # index for txt[]
        while i < len_ref:

            self.n_operations += 1
            if self.candidate[j] == self.reference[i]:
                i += 1
                j += 1


            if j == len_can:
                self.n_operations += 1
                offset_lst.append(i - j)
                j = self.lps[j - 1]
                if (not multiple_search):
                    return offset_lst
            # mismatch after j matches
            elif i < len_ref and self.candidate[j] != self.reference[i]:
                self.n_operations += 1
                if j != 0:
                    j = self.lps[j - 1]
                else:
                    i += 1
        return offset_lst

    def computeLPSArray(self):
        len_can = len(self.candidate)

        length = 0

        self.lps[0] = 0
        i = 1

        while i < len_can:
            self.n_operations += 1
            if self.candidate[i] == self.candidate[length]:
                length += 1
                self.lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = self.lps[length - 1]
                else:
                    self.lps[i] = 0
                    i += 1
