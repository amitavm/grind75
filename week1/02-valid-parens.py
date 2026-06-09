#!/usr/bin/env python

# Solve the "Valid Parentheses" problem.
#
# Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[`,
# and `]`, determine if the input string is "valid".
#
# A string is valid if:
#
# - Open brackets must be closed by the same type of closing brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has an open bracket of the same type.

def isValid(s: str) -> bool:
    # Stack to keep track of all open brackets in s in LIFO order.
    bstack = []

    # Dict to map all valid close brackets to the corresponding open brackets.
    bmap = {')': '(', ']': '[', '}': '{'}

    # All strings with an odd number of characters must be invalid.
    if len(s) % 2 != 0:
        return False

    for c in s:
        if c in bmap:
            if not bstack or bmap[c] != bstack.pop():
                return False
        else:
            bstack.append(c)
        # NOTE that we use only a two-way if-else branch here: either c is an
        # open or a close bracket.  We don't check for any other possibility
        # for c because we are told (in the problem statement) that s only
        # contains those six (open and close) bracket characters and no other.

    return not bstack
