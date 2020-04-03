# CodeWars Python Solutions

---

## Form The Largest

**Task**

Given a number , Return _The Maximum number_ could be formed from the digits of the number given.


**Notes**

* Only Natural numbers passed to the function , numbers Contain digits [0:9] inclusive
* Digit Duplications could occur , So also consider it when forming the Largest

**Input >> Output Examples:**

```python
maxNumber (213) ==> return (321)
```

**Explanation:**

As 321 is _The Maximum number_ could be formed from the digits of the number `213`.

```python
maxNumber (7389) ==> return (9873)
```

**Explanation:**

As `9873` is _The Maximum number_ could be formed from the digits of the number `7389`.

```python
maxNumber (63729) ==> return (97632)
```


**Explanation:**

As `97632` is _The Maximum number_ could be formed from the digits of the number `63729`.

```python
maxNumber (566797) ==> return (977665)
```

**Explanation:**

As `977665` is _The Maximum number_ could be formed from the digits of the number `566797`.

Note : Digit duplications are considered when forming the largest.

```python
maxNumber (17693284) ==> return (98764321)
```

**Explanation:**

As `98764321` is _The Maximum number_ could be formed from the digits of the number `17693284`.


---

### Given Code


```python
def max_number(n):
    pass
```

---

### Solution


```python
def max_number(n):
    return int("".join(sorted([i for i in str(n)], reverse=True)))
```


---


[See on CodeWars.com](https://www.codewars.com/kata/5a4ea304b3bfa89a9900008e)
