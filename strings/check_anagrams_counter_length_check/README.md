# Check Whether Two Strings Are Anagrams — Method 3 (Counter with a Length Check)

**Platform:** Custom

## Problem Statement

Check whether two strings are anagrams. First check if their lengths are equal, then compare how many times each character appears. This method treats spaces and uppercase or lowercase letters as different characters.

## My Approach — Method 3 (Counter with a Length Check)

First, we import `Counter` from Python's `collections` module. We use `Counter` because it automatically counts how many times each character appears in a string.

After that, we create a function called `is_anagram(str1: str, str2: str)`. This function takes two strings and checks whether they are anagrams or not.

Then we use `if len(str1) != len(str2):` to check whether both strings have the same length.

We check the length first because if two strings have different lengths, they cannot be anagrams.

If the lengths are different, we immediately return `False`. This means we don't need to count or compare the characters.

If both strings have the same length, we move to the next line:

`return Counter(str1) == Counter(str2)`

Here, `Counter(str1)` counts how many times each character appears in the first string, and `Counter(str2)` does the same thing for the second string.

After that, `==` compares both character counts.

If both strings have the same characters with the same counts, the function returns `True`, which means they are anagrams. Otherwise, it returns `False`.

Finally, we call `print(is_anagram("listen", "silent"))`. Both strings have the same length and character counts, so it prints `True`.

Then we call `print(is_anagram("rat", "car"))`. Both strings have the same length, but their characters are different, so it prints `False`.

This method works because we first check the length of both strings. If their lengths are different, we immediately return `False`. Otherwise, we use `Counter` to compare their character counts and check whether they are anagrams.

## Complexity

**Time Complexity: O(N)**

First, we check the length of both strings, which takes O(1) time.

If both strings have the same length, `Counter` goes through every character in each string and counts them. After that, we compare both character counts.

So the overall time complexity is O(N).

**Space Complexity: O(N)**

We use `Counter` to store the characters and their counts from both strings.

In the worst case, every character can be different, so the Counters can store up to N characters each.

Therefore, the space complexity is O(N).

Here, N means the length of one string when both strings have the same length.

## Example

**Input:**

```python
print(is_anagram("listen", "silent"))
print(is_anagram("rat", "car"))
```

**Output:**

```text
True
False
```
