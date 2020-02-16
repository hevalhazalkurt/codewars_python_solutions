# CodeWars Python Solutions

---

## List Filtering

In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.


**Example**

```python
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```


---

### Given Code


```python
def filter_list(l):
    pass
```

---

### Solution


```python
def filter_list(l):
    return [i for i in l if type(i) != str]
```


---


[See on CodeWars.com](https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/)
