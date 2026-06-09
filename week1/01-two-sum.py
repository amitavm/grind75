#!/usr/bin/env python

# Solve the "Two Sum" problem.
#
# Given an array of integers `num`, and a `target` integer, return indices of
# two elements in the array such that the sum of the elements equals target.
#
# You may assume that each input array has *exactly one solution*, and you may
# *not* use the same element twice.  The indices can be returned in any order.

def twoSum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i

    # NOTE that this is basically the "not-found return".  We have put this in
    # here just to make sure this function doesn't return a None by default.
    # But this should never actually happen during testing because we are told
    # to assume that every input array has "exactly one solution".
    return -1, -1


# NOTE that we have already shown a very good, linear-time implementation here.
# (But it does use O(n) additional space.)  Someone new to this problem will
# probably consider a brute-force, quadratic-time solution first, using two
# nested loops, comparing each element in the array with every other element.
