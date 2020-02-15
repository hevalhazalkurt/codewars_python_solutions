# CodeWars Python Solutions

---

## Do I get a bonus?

It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the most money?

Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with "£" (= `"\u00A3"`, JS, Go, and Java), "$" (C#, C++, Ruby, Clojure, Elixir, PHP and Python, Haskell, Lua) or "¥" (Rust).

---

### Given Code


```python
def bonus_time(salary, bonus):
    pass
```

---

### Solution 1


```python
def bonus_time(salary, bonus):
    return "${}".format(salary * 10) if bonus == True else "${}".format(salary)
```

---

### Solution 2


```python
def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))
```


---


[See on CodeWars.com](https://www.codewars.com/kata/56f6ad906b88de513f000d96/)
