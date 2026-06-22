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
problems.  I used Google Gemini 3.5 Flash to critique my solutions, and these
notes are based on Gemini's feedback and suggestions.

### Two Sum

- Problem: [Two Sum](https://leetcode.com/problems/two-sum)
- Solution: [week1/01-two-sum.py](week1/01-two-sum.py)

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

In my defence, it's not that I wasn't aware of this idiom.  Just that I was too
focused on getting an efficient algorithm right, and instinctively used a while
loop without giving it much thought.[^while-loop]

[^while-loop]: I had grown used to using while loops when iterating over arrays
    in the context of "DSA problems" as a more general-purpose and flexible
    alternative to the standard and popular for loops.  In some situations, the
    additional flexibility of manual updation comes handy, especially when you
    may *not* want to update the loop counter based on some condition, or
    want to make an "update" that's different from "increment an integer or
    index".  But here, that flexibility is of no use, and using the idiomatic
    for-enumerate pair is definitely better.

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
solution doesn't actually do double-lookups, mostly.  (How come?)  And it also
destroys the idiomatic simplicity of the original.  So the solution stands as
is!

### Valid Parentheses

- Problem: [Valid Parentheses](https://leetcode.com/problems/two-sum)
- Solution: [week1/02-valid-parens.py](week1/02-valid-parens.py)

I mostly got the solution right in one go: a linear-time algorithm using a
stack and a dict.  Except that its runtime percentile was a disappointing
12.3%!

Again, too much focus on getting the algorithm right made me miss checking for
the simple early-exit check: if the input string contains an odd number of
characters, it can't be valid.  Adding that check to the start of the function
caused its percentile score to shoot up to 100%!

Another bit of miss on my part was, yet again, in idiomatic Python: I wrote
`len(bstack) == 0` to check for an empty stack, bug Gemini suggested (in line
with PEP8, mind you) that it's more idiomatic to write `not bstack` instead.

### Merge Two Sorted Lists

As I have noted in the source file, this just employs the standard merge
procedure from the classic merge-sort algorithm in a linked-list context.

The moment I thought of that, I basically went into autopilot and
(embarassingly) had put in two while loops after the main (merge) loop to copy
"leftover" nodes (if any).  Gemini gently pointed out that we are now just
splicing linked lists in place (there is no "copying" happening to extra
storage space), so we just need a single O(1) assignment to take care of any
number of leftover nodes.

The other "adjustment" Gemini made was to my mental model, or perspective, of
what's actually going on.  I remarked that this is a "heavy handed" version of
the classic merge procedure.  I was mostly thinking from the syntactic and
conceptual points of view: I felt the need to define a ListNode class and the
accompanying concept of a singly-linked list, and splicing the links is
"heavier" than using simple, builtin arrays as in merge-sort.  That may be
true, but Gemini pointed out that from the runtime perspective, this procedure
is *less* heavy-handed because it's happening in-place using O(1) space (we are
just splicing the nodes in contrast to allocating O(n) extra space in
merge-sort), and (as noted above), "copying" leftover nodes is also a O(1)
operation.  Matter of perspective, I guess.
