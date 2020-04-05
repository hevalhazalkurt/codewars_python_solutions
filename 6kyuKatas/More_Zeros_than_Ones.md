# CodeWars Python Solutions

---

## More Zeros than Ones


Create a moreZeros function which will receive a string for input, and return an array (or null terminated string in C) containing only the characters from that string whose binary representation of its ASCII value consists of more zeros than ones.

You should remove any duplicate characters, keeping the first occurence of any such duplicates, so they are in the same order in the final array as they first appeared in the input string.

```python
'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
               True       True       False      True       False

        --> ['a','b','d']

'DIGEST'--> ['D','I','E','T']
```

All input will be valid strings of length > 0. Leading zeros in binary should not be counted.


---

### Given Code


```python
def more_zeros(s):
    return False
```

---

### Solution


```python
def more_zeros(s):
    chars = [c for c in s if bin(ord(c)).count("0") >= 5]
    uniques = []

    for char in chars:
        if char not in uniques: uniques.append(char)

    return uniques
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5d41e16d8bad42002208fe1a)
