# word counter
from typing import Dict, Any


def word_counter(s):
    count: Dict[Any, Any] = {}
    for i in s:
        count[i] = s.count(i)
    return count


user_input = input("Enter any String : ")
print(word_counter(user_input))
