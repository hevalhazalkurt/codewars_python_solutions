# CodeWars Python Solutions

---

## Sum of a Sequence [Hard-Core Version]


As the title suggests, this is the hard-core version of [another neat kata](https://github.com/hevalhazalkurt/codewars_python_solutions/blob/master/7kyuKatas/Sum_of_a_sequence.md).

The task is simple to explain: simply sum all the numbers from the first parameter being the beginning to the second parameter being the upper limit (possibly included), going in steps expressed by the third parameter:


**Examples**

```
sequence_sum(2, 2, 2) # 2
sequence_sum(2, 6, 2) # 12 (= 2 + 4 + 6)
sequence_sum(1, 5, 1) # (= 1 + 2 + 3 + 4 + 5)
sequence_sum(1, 5, 3) # 5 (= 1 + 4)
```


If it is an impossible sequence (with the beginning being larger the end and a positive step or the other way around), just return `0`. See the provided test cases for further examples :)

Note: differing from the other base kata, much larger ranges are going to be tested, so you should hope to get your algo optimized and to avoid brute-forcing your way through the solution.


---

### Given Code


```python
def sequence_sum(begin_number, end_number, step):
    #your code here
```

---

### Solution 1


```python
def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))
```

---

### Solution 2


```python
def sequence_sum(begin_number, end_number, step):
    n = (end_number - begin_number) // step
    return 0 if n < 0 else (n+1)*(n*step+begin_number+begin_number)//2
```


---


[See on CodeWars.com](https://www.codewars.com/kata/587a88a208236efe8500008b)
