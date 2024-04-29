from collections import deque


def is_palindrome(s):
    cleaned_string = ''.join(ch.lower() for ch in s if ch.isalnum())

    char_deque = deque(cleaned_string)

    while len(char_deque) > 1:
        front = char_deque.popleft()
        back = char_deque.pop()
        if front != back:
            return False

    return True


test_strings = ["A man, a plan, a canal, Panama", "Was it a car or a cat I saw?", "No lemon, no melon", "Python"]
for test in test_strings:
    print(f"'{test}' -> {is_palindrome(test)}")
