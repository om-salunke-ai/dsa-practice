# Print Characters That Appear Only Once

**Platform:** Custom  
**Topic:** Strings  
**Language:** Python

## Problem Statement

Print characters that appear only once.

## My Approach

The first if-else logic is the same as before. We first store all the characters and their counts in a dictionary.

After that, we run another `for` loop through the dictionary, where all the characters are stored. We access each character one at a time and check its count.

If `dic[i] == 1`, we print that character because it appears only once.

We first count all the characters because later we need to check which characters appear multiple times and which characters are unique.

`if dic[i] == 1` checks whether a character appears only once. If a character appears only once, it is a non-repeating character, and that is what we need to print.

## Complexity

**Time Complexity: O(N)**

The first loop goes through every character in the text to count them. The second loop goes through the characters stored in the dictionary. So the overall time complexity is O(N).

**Space Complexity: O(N)**

We use a dictionary to store the characters and their counts. In the worst case, every character can be different, so the dictionary can store up to N characters. Therefore, the space complexity is O(N).

## Example

Input:

```text
hello
```

Output:

```text
h
e
o
```

## Solution

[View the Python solution](solution.py)
