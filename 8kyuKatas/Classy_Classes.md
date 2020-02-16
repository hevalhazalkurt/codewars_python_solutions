# CodeWars Python Solutions

---

## Classy Classes

Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes

**Task**

Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return


```
johns age is 34
```

---

### Given Code


```
class Person
    def __init__(name,age)
        self.info = "#{name}s age is #{age}"
```

---

### Solution


```python
class Person:
    def __init__(self, name,age):
        self.info = "{}s age is {}".format(name, age)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/55a144eff5124e546400005a/)
