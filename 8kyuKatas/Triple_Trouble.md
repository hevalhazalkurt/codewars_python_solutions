# CodeWars Python Solutions

---

## Triple Trouble

Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

E.g. Input: `"aa"`, `"bb"` , `"cc"` => Output: `"abcabc"`

Note: You can expect all of the inputs to be the same length.


---

### Given Code


```python
def triple_trouble(one, two, three):
    pass
```

---

### Solution 1


```python
def triple_trouble(one, two, three):
    return "".join([one[i]+two[i]+three[i] for i in range(len(one))])
```


### Solution 2


```python
def triple_trouble(one, two, three):
    return "".join(a+b+c for a,b,c in zip(one,two,three))
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5704aea738428f4d30000914/)
