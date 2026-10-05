# Print All Repeated Characters

## Problem Statement

Given a text, print all characters that appear more than once along with their count.

## My Approach

First, we go through the text and store each character and its count in a dictionary.

After storing all the characters, we run another loop through the dictionary and check whether each character appears more than once.

If `dic[i] > 1`, it means that character is repeated, so we print the character `i` and its count `dic[i]`.

For example, if the input is `"omm"`, the character `m` appears two times, so the output will show `m 2`.

This works because the dictionary already stores the count of every character. The condition `dic[i] > 1` makes sure that we print only the characters that appear more than once.

## Complexity

**Time Complexity: O(N)**

The first loop goes through every character in the text to count them. The second loop goes through the characters stored in the dictionary. So the overall time complexity is O(N).

**Space Complexity: O(N)**

We use a dictionary to store the characters and their counts. In the worst case, every character can be different, so the dictionary can store up to N characters. Therefore, the space complexity is O(N).

## Example

**Input:**

```text
omm
```

**Output:**

```text
m 2
```
