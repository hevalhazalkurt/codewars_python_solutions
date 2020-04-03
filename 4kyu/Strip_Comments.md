# CodeWars Python Solutions

---

## Strip Comments

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

**Example**

Given an input string of :

```
apples, pears # and bananas
grapes
bananas !apples
```

The output expected would be :

```
apples, pears
grapes
bananas
```


The code would be called like so :

```python
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
```

---

### Given Code


```python
def solution(string,markers):
    pass
```

---

### Solution 1


```python
def solution(string,markers):
    s_list = string.split("\n")
    n_list = []

    for item in s_list:
        s = ""
        for char in item:
            if char in markers:
                break
            else:
                s = s + char
        n_list.append(s.strip())
    return "\n".join(n_list)
```


---

### Solution 2


```python
def solution(string,markers):
    s_list = string.split('\n')
    for marker in markers:
        s_list = [item.split(marker)[0].strip() for item in s_list]
    return '\n'.join(s_list)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/51c8e37cee245da6b40000bd/)
