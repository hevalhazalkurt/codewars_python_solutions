# CodeWars Python Solutions

---

## Find the divisors!


**Definition**

Create a function named `divisors`/`Divisors` that takes an integer `n > 1` and returns an array with all of the integer's divisors (except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (`null` in C#) (use `Either String a` in Haskell and `Result<Vec<u32>, String>` in Rust).

Example:

```Python
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
```

---

### Given Code


```python
def divisors(integer):
    pass
```

---

### Solution 1


```python
def divisors(integer):
    l = [n for n in range(2,integer) if integer % n == 0]
    return l if len(l) > 0 else "{} is prime".format(integer)
```


---

### Solution 2


```python
def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n
```


---


[See on CodeWars.com](https://www.codewars.com/kata/544aed4c4a30184e960010f4)
