# CodeWars Python Solutions

---

## Transportation on vacation

After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).

---

### Given Code


```python
def rental_car_cost(d):
    pass
```

---

### Solution


```python
def rental_car_cost(d):
    if 3 <= d < 7:
        return (d * 40) - 20
    elif d >= 7:
        return (d * 40) - 50
    else:
        return d * 40
```


---


[See on CodeWars.com](https://www.codewars.com/kata/568d0dd208ee69389d000016/)
