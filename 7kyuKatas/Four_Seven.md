# CodeWars Python Solutions

---

## Four/Seven

Simple kata, simple rules: your function should accept the inputs `4` and `7`. If `4` is entered, the function should return `7`. If `7` is entered, the function should return `4`. Anything else entered as input should return a false-y value such as `False`, `0`, `[]`, `""`. There's only one catch, your function cannot include if statements (or the eval function due to the fact that you can get around the if requirement using it).

There are some very simple ways of answering this problem, but I encourage you to try and be as creative as possible.

Good Luck!


---

### Given Code


```python
def solution(n):
    pass
```

---

### Solution


```python
def solution(n):
    nums = {4: 7, 7:4}
    return nums.get(n, False)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5ff50f64c0afc50008861bf0)
