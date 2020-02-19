# CodeWars Python Solutions

---

## Selective fear of numbers

I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated: The number I'm feared of depends on which day of week it is... This a concrete description of my mental illness:

Monday --> 12

Tuesday --> numbers greater than 95

Wednesday --> 34

Thursday --> 0

Friday --> numbers divisable by 2

Saturday --> 56

Sunday --> 666 or -666

Write a function which takes a string (day of week) and an integer (number to be tested) so it tells the doctor if I'm feared or not. (return a boolean)

---

### Given Code


```python
def am_I_afraid(day,num):
    pass
```

---

### Solution


```python
def am_I_afraid(day,num):
    if day == "Monday": return num == 12
    if day == "Tuesday": return num > 95
    if day == "Wednesday": return num == 34
    if day == "Thursday": return num == 0
    if day == "Friday": return num % 2 == 0
    if day == "Saturday": return num == 56
    if day == "Sunday": return num == 666 or num == -666
```


---


[See on CodeWars.com](https://www.codewars.com/kata/55b1fd84a24ad00b32000075/)
