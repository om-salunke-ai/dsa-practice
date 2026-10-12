# Check Whether Two Strings Are Anagrams

**Platform:** Custom

**Method:** Two Dictionaries

## Problem Statement

Check whether two strings are anagrams. Two strings are anagrams when they contain the same characters with the same counts, even if their order is different.

## My Approach

First, the user enters two strings, `text1` and `text2`.

After that, we create two empty dictionaries, `dic1` and `dic2`, to store each character and its count from both strings separately.

Then we run the first `for` loop through `text1` and access each character one at a time. If the character is already present in `dic1`, we increase its count by 1. If it appears for the first time, we add it to the dictionary with a count of 1.

We do the same thing for `text2` using another `for` loop and store its character counts in `dic2`.

After storing all the character counts in both dictionaries, we use `if dic1 == dic2:` to compare them.

If both dictionaries are equal, it means both strings have the same characters with the same counts, so we print `"Anagram"`.

Otherwise, we print `"Not anagram"`.

This works because two strings are anagrams when they contain the same characters with the same frequency, even if the order of the characters is different.

## Complexity

**Time Complexity: O(N)**

The first loop goes through every character in `text1`, and the second loop goes through every character in `text2`. After that, we compare both dictionaries. So the overall time complexity is O(N).

**Space Complexity: O(N)**

We use two dictionaries to store the characters and their counts. In the worst case, the dictionaries can store up to N characters together. Therefore, the space complexity is O(N).

Here, N means the total number of characters in both input strings combined.

## Example

**Input:**

```text
listen
silent
```

**Output:**

```text
Anagram
```
