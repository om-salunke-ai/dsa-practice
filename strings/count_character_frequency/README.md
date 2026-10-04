# Count the Frequency of Each Character

**Platform:** Custom  
**Topic:** Strings  
**Language:** Python

## Problem Statement

Count the frequency of each character.

## Example

Input:

```text
banana
```

Output:

```text
{'b': 1, 'a': 3, 'n': 2}
```

## My Approach

The user enters any word or text. Then we create an empty dictionary to store all the characters and their counts.

After that, we run a `for` loop that goes through the text one character at a time.

For each character, we check if it is already present in the dictionary. If it is already there, we increase its count by 1. If it is not present, we add it to the dictionary with a count of 1.

Finally, we print the dictionary.

I use a dictionary because it can store each character with its count.

If a character appears for the first time, its count is set to 1. If the same character appears again, its count increases by 1 each time.

This works because the loop checks every character in the text. If a character appears multiple times, its count keeps increasing. If it appears only once, its count stays 1.

## Solution

[View the Python solution](solution.py)

## Time Complexity: O(N)

The loop goes through each character in the text one time. Dictionary checking and updating takes O(1) average time, so the total time complexity is O(N).

## Space Complexity: O(N)

We use a dictionary to store the characters and their counts. In the worst case, if every character is different, the dictionary can store up to N characters. So the space complexity is O(N).
