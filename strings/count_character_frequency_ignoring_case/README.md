# Count Character Frequency While Ignoring Letter Case

## Problem Statement

Count how many times each character appears in the text while ignoring uppercase and lowercase differences.

## My Approach

First, the user enters any text. We use `.lower()` to convert the complete text into lowercase.

We do this because we want uppercase and lowercase letters to be treated as the same character. For example, `A` and `a` will both become `a`.

After that, we create an empty dictionary to store each character and its count.

Then we run a `for` loop through the text and access each character one at a time.

If the character is already present in the dictionary, we increase its count by 1.

If the character appears for the first time, we add it to the dictionary with a count of 1.

Finally, we print the dictionary.

This works because `.lower()` first makes all letters lowercase, so the code counts uppercase and lowercase versions of the same letter together.

## Complexity

**Time Complexity: O(N)**

`.lower()` goes through the text to convert the letters to lowercase, and the `for` loop also goes through every character once. So the overall time complexity is O(N).

**Space Complexity: O(N)**

We use a dictionary to store the characters and their counts. In the worst case, every character can be different, so the dictionary can store up to N characters. Therefore, the space complexity is O(N).

## Example

**Input:**

```text
AaBbA
```

**Output:**

```text
{'a': 3, 'b': 2}
```
