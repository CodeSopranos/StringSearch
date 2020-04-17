from collections import defaultdict
from algorithm.base import Algorithm
from string import ascii_letters


class KnuthMorrisPratt(Algorithm):

    def __init__(self, reference):
        # reference = reference.translate(reference.maketrans('', '', ascii_letters))
        self.reference = reference

    @property
    def name(self):
        return 'Knuth-Morris-Pratt'
    
    def set_candidate(self, candidate, **params):
        self.candidate = candidate

    def search(self, multiple_search=False) -> list:
        """Return the lowest index of T at which substring P begins (or else -1)."""
        len_reference = len(self.reference)
        len_candidate = len(self.candidate)
        if len_candidate > len_reference:
            print("Error: len candidate > len references {} > {}.".format(len_candidate, len_reference))
            return -1
         # create lps[] that will hold the longest prefix suffix
        # values for pattern
        self.lps = [0] * len_candidate
        j = 0  # index for pat[]

        # Preprocess the pattern (calculate lps[] array)
        self.computeLPSArray()
        
        offset_lst = []
        
        i = 0  # index for txt[]
        while i < len_reference:
            if self.candidate[j] == self.reference[i]:
                i += 1
                j += 1

            if j == len_candidate:
                offset_lst.append(i - j)
                j = self.lps[j - 1]
                if (not multiple_search): 
                    return offset_lst
            # mismatch after j matches
            elif i < len_reference and self.candidate[j] != self.reference[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = self.lps[j - 1]
                else:
                    i += 1
        return offset_lst
        
    def computeLPSArray(self):
        len_candidate = len(self.candidate)

        length = 0  # length of the previous longest prefix suffix

        self.lps[0] = 0  # lps[0] is always 0
        i = 1

        # the loop calculates lps[i] for i = 1 to M-1
        while i < len_candidate:
            if self.candidate[i] == self.candidate[length]:
                length += 1
                self.lps[i] = length
                i += 1
            else:
                if length != 0:
                    # This is tricky. Consier the example AAACAAAA
                    # and i = 7
                    length = self.lps[length - 1]

                    # Also, note that we do not increment i here
                else:
                    self.lps[i] = 0
                    i += 1
