# CodeWars Python Solutions

---

## Dashatize it

Given a variable `n`,

If `n` is an integer, Return a string with dash `'-'` marks before and after each odd integer, but do not begin or end the string with a dash mark. If `n` is negative, then the negative sign should be removed.

If `n` is not an integer, return an empty value.

Ex:

```python
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
```


---

### Given Code


```python
def dashatize(n):
    pass
```

---

### Solution 1


```python
def dashatize(n):
    print(n)
    if type(n) == int:
        n = str(abs(n))
        new = ""
        for e,i in enumerate(n):
            if int(i) % 2 != 0:
                if e == 0:
                    new += "{}-".format(i)
                elif e == len(n)-1:
                    new += "-{}".format(i)
                else:
                    new += "-{}-".format(i)
            else:
                new += i
        if new[-1] == "-": new = new[:-1]
        return new.replace("--", "-")
    else:
        return "None"
```


### Solution 2


```python
def dashatize(num):
    num_str = str(num)
    for i in ['1','3','5','7','9']:
        num_str = num_str.replace(i,'-' + i + '-')
    return num_str.strip('-').replace('--','-')
```


---


[See on CodeWars.com](https://www.codewars.com/kata/58223370aef9fc03fd000071)
