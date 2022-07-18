# CodeWars Python Solutions

---

## IP Validation

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:

```
Examples of valid inputs:
1.2.3.4
123.45.67.89
```

Invalid input examples:

```
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
```

Notes:
* Leading zeros (e.g. `01.02.03.04`) are considered invalid
* Inputs are guaranteed to be a single string

---

### Given Code


```python
def is_valid_IP(strng):
    return None
```

---

### Solution 1


```python
def is_valid_IP(strng):
    try:
        formatted = [int(i.strip()) for i in strng.split(".") if 0 <= int(i) <= 255]
        if len(formatted) == 4 and ".".join([str(i) for i in formatted]) == strng:
            return True
        else:
            return False
    except:
        return False
```


### Solution 2

```python
from ipaddress import ip_address

def is_valid_IP(strng):
    try:
        return True if ip_address(strng) else False
    except:
        return False
```

---


[See on CodeWars.com](https://www.codewars.com/kata/515decfd9dcfc23bb6000006/)
