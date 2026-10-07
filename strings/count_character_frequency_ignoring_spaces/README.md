# Count Character Frequency While Ignoring Spaces

## Problem Statement

Count how many times each character appears in the text, but do not count spaces.

## My Approach

First, the user enters any text. Then we create an empty dictionary to store each character and its count.

After that, we run a `for` loop through the text and access each character one at a time.

Before adding the character to the dictionary, we check `if i != " ":`. This condition checks that the current character is not a space.

If the character is a space, we do nothing and the loop moves to the next character.

If it is not a space, we check whether that character is already present in the dictionary.

If the character is already in the dictionary, we increase its count by 1. If it appears for the first time, we add it to the dictionary with a count of 1.

Finally, we print the dictionary.

This works because every non-space character is counted, while spaces are skipped because of the `if i != " ":` condition.

## Complexity

**Time Complexity: O(N)**

The loop goes through every character in the text one time. Checking the character and updating the dictionary takes O(1) average time, so the total time complexity is O(N).

**Space Complexity: O(N)**

We use a dictionary to store the characters and their counts. In the worst case, every non-space character can be different, so the dictionary can store up to N characters. Therefore, the space complexity is O(N).

## Example

**Input:**

```text
hello world
```

**Output:**

```text
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```
