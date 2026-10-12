# Check Whether Two Strings Are Anagrams — Method 2 (Counter)

**Platform:** Custom

## Problem Statement

Check whether two strings are anagrams while ignoring spaces and uppercase or lowercase differences.

## My Approach

First, we import `Counter` from Python's `collections` module. We use `Counter` because it automatically counts how many times each character appears in a string, so we don't need to write our own dictionary and `for` loop.

After that, we create a function called `is_anagram(str1: str, str2: str)`. This function takes two strings, `str1` and `str2`, and checks whether they are anagrams or not. Here, `str` just tells us that both inputs should be strings.

Then we write `s1 = str1.replace(" ", "").lower()`.

In this line, `replace(" ", "")` removes all spaces from the first string, and `.lower()` converts all uppercase letters into lowercase. We store the result in `s1`.

We do the same thing for the second string using `s2 = str2.replace(" ", "").lower()` and store the result in `s2`.

We remove spaces and convert letters to lowercase because we want to ignore spaces and uppercase or lowercase differences while checking anagrams.

After that, we use `return Counter(s1) == Counter(s2)`.

Here, `Counter(s1)` counts how many times each character appears in the first string, and `Counter(s2)` does the same thing for the second string.

Then `==` compares both character counts.

If both strings have the same characters with the same counts, the function returns `True`, which means they are anagrams. Otherwise, it returns `False`.

Finally, we call the function using `print(is_anagram("Listen", "Silent"))`. Both strings have the same characters after converting them to lowercase, so it prints `True`.

Then we call `print(is_anagram("Hello", "World"))`. These strings do not have the same characters and counts, so it prints `False`.

This method works because `Counter` counts all the characters for us, and we only need to compare those counts to check whether two strings are anagrams.

## Complexity

**Time Complexity: O(N)**

First, we remove spaces and convert both strings into lowercase. After that, `Counter` goes through each string and counts every character. Finally, we compare both character counts. So the overall time complexity is O(N).

**Space Complexity: O(N)**

We create two new strings after removing spaces and converting them to lowercase. We also use `Counter` to store the characters and their counts. In the worst case, the extra memory grows with the number of characters, so the space complexity is O(N).

Here, N means the total number of characters in both input strings combined.

## Example

**Input:**

```python
print(is_anagram("Listen", "Silent"))
print(is_anagram("Hello", "World"))
```

**Output:**

```text
True
False
```
