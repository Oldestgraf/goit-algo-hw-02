from collections import deque

def is_palindrome(s):
    norm_str = ''.join(char.lower() for char in s if char.isalnum())
    d = deque(norm_str)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
        return True

print(is_palindrome("foot"))
print(is_palindrome("foof"))
