# The Grind 75 Problemset

## Overview

Here you will find my solutions to the "Grind 75" leetcode problems.  If you
are prepping for tech interviews, you should probably attempt them on your own
first before looking through my (or anyone else's) solutions, for at least two
reasons:

- Doing them on your own will give you the opportunity to develop your mental
  muscles for analytical thinking and solving problems.
- For all you know, my solutions could be incorrect!  If so, they could mislead
  you and waste your time.  I have just shown my *attempts* here: I make no
  claims of correctness!

I've followed the numbering and layout in the [grind75
website](https://www.techinterviewhandbook.org/grind75/).  So the problems are
split into directories `week1`, `week2`, etc.  Inside those directoies I have
numbered the problems `01`, `02`, etc., exactly matching the numbering in the
website.  _Please note_ that these mostly don't correspond to their numbering
in [Leetcode](https://leetcode.com/), except perhaps the two-sum problem.

## Notes

These are some notes based on my learnings from working on the grind75
problems.  I used Google Gemini 3.5 Flash to critique my solutions, and most of
these notes are based on those Gemini's feedback and suggestions.

### Two Sum

Problem: [Two Sum](https://leetcode.com/problems/two-sum)
Solution: [week1/01-two-sum.py](week1/01-two-sum.py)

I got the key idea right: using a dict to record previously seen numbers and
their indices so that processing each number in `nums`---checking if its
complement occurs earlier in `nums`, and if not, adding it to the dict---takes
a constant time.  So it was a linear-time algorithm from the start, and was
accepted (by Leetcode).  Its runtime percentile score was reported to be 100%.

Where I didn't do so well was in writing idiomatic Python.  I used a `while`
loop and manually incremented the loop counter, like this:

```python
def twoSum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}
    i, n = 0, len(nums)
    while i < n:
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
        i += 1
    return -1, -1
```

Gemini suggested using `enumerate` instead, paired with a `for` loop (as seen
in the solution).  This makes the code more concise as well as idiomatic.

It's not that I wasn't aware of this idiom; just that I had grown used to using
while loops when doing some array problems.  In some situations, the additional
flexibility of manual updation comes handy, especially when you may *not* want
to update the loop counter based on some condition.  But here, that flexibility
is completely useless, and using the idiomatic for-enumerate pair is definitely
better.

During the review stage, I also got into an "over-optimization" diversion and
ended up introducing a subtle bug because of that.  I thought, "Why do the dict
lookup twice?  We can use the recently introduced walrus-op and do only one
lookup!" And this is what the code looked like after that change:

```python
def twoSum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}
    for i, num in enumerate(nums):
        if (cidx := seen.get(target - num)):
            return cidx, i
        seen[num] = i
    return -1, -1
```

Can you spot the bug?  The fix is simple once you see it:

```python
if (cidx := seen.get(target - num)) is not None:
```

Gemini successfully caught the bug, and correctly explained that the original
version doesn't actually do double lookups, mostly.  (How come?)  And it also
destroys the idiomatic simplicity of the original.  So the solution stands as
is.
