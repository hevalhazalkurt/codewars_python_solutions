# CodeWars Python Solutions

---

## Convert Hash To An Array


Convert a hash into an array. Nothing more, Nothing less.


```python
{name: 'Jeremy', age: 24, role: 'Software Engineer'}
```

should be converted into

```python
[["name", "Jeremy"], ["age", 24], ["role", "Software Engineer"]]
```

Note: The output array should be sorted alphabetically.

Good Luck!


---

### Given Code


```python
def convert_hash_to_array(hash):
    pass
```

---

### Solution


```python
def convert_hash_to_array(hash):
    return sorted([[k, v] for k,v in hash.items()])
```


---


[See on CodeWars.com](https://www.codewars.com/kata/59557b2a6e595316ab000046)
