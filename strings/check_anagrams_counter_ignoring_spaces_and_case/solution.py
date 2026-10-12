# Platform: Custom | Link: N/A
from collections import Counter

def is_anagram(str1: str, str2: str):
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()

    return Counter(s1) == Counter(s2)

print(is_anagram("Listen", "Silent"))
print(is_anagram("Hello", "World"))
