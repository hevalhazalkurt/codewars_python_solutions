# CodeWars Python Solutions

---

## Replacement

**Introduction**

Little Petya very much likes sequences. Recently he has received one as a gift from his mother.

Petya didn't like it at once. He decided to make a replacement. After the replacement Petya sorted the sequence by the numbers' non-decreasing.

Now he is asking himself: What is the minimal possible value I could have got after the replacement and sorting the sequence?

**About the replacement**

Choose exactly one element from the sequence and replace it with another integer > 0. It is not allowed to replace a number with itself or to change no number at all.

**Task**

Find the minimal possible sequence after performing a valid replacement and sorting the sequence.

**Input:**

Input contains sequence with N integers. All elements of the sequence > 0. The sequence will never be empty.

**Output:**

Return sequence with N integers — the minimum possible values of each sequence element after one replacement and the sorting are performed.

**Example**

```
([1,2,3,4,5])  =>  [1,1,2,3,4]
([4,2,1,3,5])  =>  [1,1,2,3,4]
([2,3,4,5,6])  =>  [1,2,3,4,5]
([2,2,2])      =>  [1,2,2]
([42])         =>  [1]
```


---

### Given Code


```python
def sort_number(a):
    pass
```

---

### Solution 1


```python
def sort_number(a):
    a = sorted(a)

    if a[-1] == 1:
        return a[:-1] + [2]
    else:
        return [1] + a[:-1]
```


---

### Solution 2


```python
def sort_number(a):
    a = sorted(a)
    return [1]+a if a.pop()!=1 else a+[2]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/598d89971928a085c000001a/)
