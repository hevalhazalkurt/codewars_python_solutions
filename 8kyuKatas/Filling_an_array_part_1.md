# CodeWars Python Solutions

---

## Filling an array (part 1)


We want an array, but not just any old array, an array with contents!

Write a function that produces an array with the numbers `0` to `N-1` in it.

For example, the following code will result in an array containing the numbers `0` to `4`:

```
arr(5) // => [0,1,2,3,4]
```



---

### Given Code


```python
def arr(n):
    # [ the numbers 0 to N-1 ]
```

---

### Solution 1


```python
def arr(n=0):
    return [i for i in range(n)] if n else []
```

---


### Solution 2


```python
def arr(n=0):
    return list(range(n))
```

---



[See on CodeWars.com](https://www.codewars.com/kata/571d42206414b103dc0006a1)
