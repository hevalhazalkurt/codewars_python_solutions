# CodeWars Python Solutions

---

## My Languages


**Your task**

You are given a dictionary/hash/object containing some languages and your test results in the given languages. Return the list of languages where your test score is at least 60, in descending order of the results.

Note: There will be no duplicate values.


**Example**

```python
{"Java": 10, "Ruby": 80, "Python": 65}  --> ["Ruby", "Python"]
{"Hindi": 60, "Dutch" : 93, "Greek": 71} --> ["Dutch", "Greek", "Hindi"]
{"C++": 50, "ASM": 10, "Haskell": 20}   --> []
```




---

### Given Code


```python
def my_languages(results):
    pass
```

---

### Solution


```python
def my_languages(results):
    return sorted([k for k,v in results.items() if v >= 60], key=lambda x: results[x], reverse=True)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5b16490986b6d336c900007d)
