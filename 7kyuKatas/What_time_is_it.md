# CodeWars Python Solutions

---

## What time is it?

Given a time in AM/PM format as a string, convert it to military (24-hour) time as a string.

Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock

Sample Input: 07:05:45PM Sample Output: 19:05:45

Try not to use built in DateTime libraries.

For more information on military time, check the wiki https://en.wikipedia.org/wiki/24-hour_clock#Military_time



---

### Given Code


```python
def get_military_time():
    # code solution here
    return
```

---

### Solution


```python
def get_military_time(s):
    if "AM" in s:
        s = s.replace("AM", "")
        l = s.split(":")
        if l[0] == "12":
            l[0] = "00"
    elif "PM" in s:
        s = s.replace("PM", "")
        l = s.split(":")
        l[0] = str(int(l[0]) + 12)
        if l[0] == "24":
            l[0] = "12"
    return ":".join(l)
```

---


[See on CodeWars.com](https://www.codewars.com/kata/57729a09914da60e17000329)
