# CodeWars Python Solutions

---

## Palindrome Strings


A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This includes capital letters, punctuation, and word dividers.

Implement a function that checks if something is a palindrome.

```python
isPalindrome("anna")   ==> true
isPalindrome("walter") ==> false
isPalindrome(12321)    ==> true
isPalindrome(123456)   ==> false
```

---

### Given Code


```python
def is_palindrome(string):
    pass
```

---

### Solution


```python
def is_palindrome(string):
    return str(string) == str(string)[::-1]
```

---


[See on CodeWars.com](https://www.codewars.com/kata/57a5015d72292ddeb8000b31/)
