#!/usr/bin/env python

# Leetcode Problem 242: Valid Anagram

from collections import defaultdict


# Return True if strings `s` and `t` are anagrams, else return False.
#
# Per the problem statement, s and t are assumed to contain only lowercase
# (English) letters, but our solution is general, and doesn't require that
# constraint.
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # Return the frequencies of characters in string `x`.
    def charFreq(x: str) -> defaultdict:
        cf = defaultdict(int)
        for c in x:
            cf[c] += 1
        return cf

    cf_s = charFreq(s)
    cf_t = charFreq(t)
    for c, f in cf_s.items():
        if cf_t[c] != f:
            return False

    return True


# Here's a version that explicitly uses that assumption that there are only 26
# possible characters that can appear in the input strings, and so uses builtin
# lists to store the letter frequencies (instead of default-dicts).  But I was
# surprised to see no visible difference in the runtime or memory used!
def isAnagram_v2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    def letterFreq(x: str) -> list[int]:
        lf = [0] * 26
        for l in x:
            lf[ord(l) - ord('a')] += 1
        return lf

    lf_s = letterFreq(s)
    lf_t = letterFreq(t)
    for i in range(len(lf_s)):
        if lf_s[i] != lf_t[i]:
            return False

    return True


# Even inlining the letterFreq function's body (as in the version below) didn't
# seem to make (much of) a difference!
def isAnagram_v3(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    NUM_LETTERS = 26

    lf_s = [0] * NUM_LETTERS
    for l in s:
        lf_s[ord(l) - ord('a')] += 1

    lf_t = [0] * NUM_LETTERS
    for l in t:
        lf_t[ord(l) - ord('a')] += 1

    for i in range(NUM_LETTERS):
        if lf_s[i] != lf_t[i]:
            return False

    return True


# The second version probably goes to show that Python's dictionary
# implementation is really good, as it should be!
#
# And the fact that the third version didn't change things, especially the
# runtime, is probably obvious in hindsight: even if the inlining gets rid of
# function-call overheads, it's only two function calls, so it can't possibly
# have any noticeable impact on the runtime.
