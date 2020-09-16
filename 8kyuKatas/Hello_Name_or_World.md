# CodeWars Python Solutions

---

## Hello, Name or World!


**Task**

Define a method `hello` that returns `"Hello, Name!"` to a given `name`, or says `Hello, World!` if `name` is not given (or passed as an empty String).

Assuming that `name` is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

Examples:

```python
hello "john"   => "Hello, John!"
hello "aliCE"  => "Hello, Alice!"
hello          => "Hello, World!" # name not given
hello ''       => "Hello, World!" # name is an empty String
```

---

### Given Code


```python
def hello(name):
    pass
```

---

### Solution


```python
def hello(name=""):
    return f"Hello, {name.title()}!" if name or len(name)> 1 else "Hello, World!"
```

---


[See on CodeWars.com](https://www.codewars.com/kata/57e3f79c9cb119374600046b)
