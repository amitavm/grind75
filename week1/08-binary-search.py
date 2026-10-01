#!/usr/bin/env python

# Leetcode Problem 704: Binary Search

def binSearch(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2 # NOTE: make sure to use integer division.
        # This simpler version would also work fine in Python:
        # mid = (lo + hi) // 2
        if nums[mid] > target:
            hi = mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            return mid
    return -1
