# CodeWars Python Solutions

---

## Are the numbers in order?

Given a string, you need to write a method that order every letter in this string in ascending order.

Also, you should validate that the given string is not empty or null. If so, the method should return:


```
"Invalid String!"
```

**Notes**

* the given string can be lowercase and uppercase.
* the string could include spaces or other special characters like '# ! or ,'


**Examples**

```
"hello world" => " dehllloorw"
"bobby"       => "bbboy"
""            => "Invalid String!"
"!Hi You!"    => " !!HYiou"
```

---

### Given Code


```python
def in_asc_order(arr):
    pass
```

---

### Solution


```python
def in_asc_order(arr):
    return arr == sorted(arr)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/56b7f2f3f18876033f000307/)
