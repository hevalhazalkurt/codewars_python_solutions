# CodeWars Python Solutions

---

## Product Of Maximums Of Array (Array Series # 2)

**Task**

Given an array/list [] of integers , Find the product of the k maximal numbers.


**Notes**

- Array/list size is at least 3 .
- Array/list's numbers Will be mixture of positives , negatives and zeros
- Repetition of numbers in the array/list could occur.



**Input >> Output Examples**

```python
maxProduct ({4, 3, 5}, 2) ==>  return (20)
```

Since the size (`k`) equal 2 , then the subsequence of size 2 whose gives product of maxima is `5 * 4 = 20` .



```python
maxProduct ({8, 10 , 9, 7}, 3) ==>  return (720)
```

Since the size (`k`) equal 3 , then the subsequence of size 2 whose gives product of maxima is `8 * 9 * 10 = 720` .

```python
maxProduct ({10, 8, 3, 2, 1, 4, 10}, 5) ==> return (9600)
```

Since the size (`k`) equal 5 , then the subsequence of size 2 whose gives product of maxima is `10 * 10 * 8 * 4 * 3 = 9600` .


```python
maxProduct ({-4, -27, -15, -6, -1}, 2) ==> return (4)
```

Since the size (`k`) equal 2 , then the subsequence of size 2 whose gives product of maxima is `-4 * -1 = 4` .

```python
maxProduct ({10, 3, -1, -27} , 3)  return (-30)
```

Since the size (`k`) equal 3 , then the subsequence of size 2 whose gives product of maxima is `10 * 3 * -1 = -30` .


---

### Given Code


```python
def max_product(lst, n_largest_elements):
    return n_largest_elements
```

---

### Solution


```python
def max_product(lst, n_largest_elements):
    sor_lst = sorted(lst, reverse=True)[:n_largest_elements]
    mul = 1
    for n in sor_lst:
        mul *= n
    return mul
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5a63948acadebff56f000018)
