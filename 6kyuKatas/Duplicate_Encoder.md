# CodeWars Python Solutions

---

## Duplicate Encoder


**Definition**

The goal of this exercise is to convert a string to a new string where each character in the new string is `"("` if that character appears only once in the original string, or `")"` if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.



**Example**

```Python
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
```


**Notes**

Assertion messages may be unclear about what they display in some languages. If you read `"...It Should encode XXX"`, the `"XXX"` is the expected result, not the input!


---

### Given Code


```python
def duplicate_encode(word):
    pass
```

---

### Solution


```python
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(l)==1 else ")" for l in word.lower()])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/54b42f9314d9229fd6000d9c)
