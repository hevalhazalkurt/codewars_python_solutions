# CodeWars Python Solutions

---

## Which are in?


**Definition**

Given two arrays of strings `a1` and `a2` return a sorted array `r` in lexicographical order of the strings of `a1` which are substrings of strings of `a2`.

**Example 1:** `a1 = ["arp", "live", "strong"]`

`a2 = ["lively", "alive", "harp", "sharp", "armstrong"]`

returns `["arp", "live", "strong"]`

**Example 2:** `a1 = ["tarp", "mice", "bull"]`

`a2 = ["lively", "alive", "harp", "sharp", "armstrong"]`

returns `[]`

**Notes:**

- Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
- In Shell bash `a1` and `a2` are strings. The return is a string where words are separated by commas.
- Beware: `r` must be without duplicates.
- Don't mutate the inputs.

---

### Given Code


```python
def in_array(array1, array2):
    pass
```

---

### Solution


```python
def in_array(array1, array2):
    arr = []
    for a2 in array2:
        for a1 in array1:
            if a1 in a2 and a1 not in arr:
                arr.append(a1)
    return sorted(arr)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/550554fd08b86f84fe000a58)
