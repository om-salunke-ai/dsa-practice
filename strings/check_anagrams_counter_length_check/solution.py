# Platform: Custom | Link: N/A
from collections import Counter

def is_anagram(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)

print(is_anagram("listen", "silent"))
print(is_anagram("rat", "car"))
