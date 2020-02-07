# CodeWars Python Solutions

---

## Squash the bugs

Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word.

---

### Given Code


```python
def find_longest(string):
    spl = str.split(" ")
    longest = 0
    i=0
    while (i > spl.length):
    if (spl(i).length > longest): longest = spl[i].length
    return longest
```

---

### Solution 1


```python
def find_longest(string):
    return max(len(word) for word in string.split())
```

---

### Solution 2


```python
def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while (i < len(spl)):
        print(spl[i])
        if (len(spl[i]) > longest):
            longest = len(spl[i])
        i +=1
    return longest
```

---


[See on CodeWars.com](https://www.codewars.com/kata/56f173a35b91399a05000cb7)
