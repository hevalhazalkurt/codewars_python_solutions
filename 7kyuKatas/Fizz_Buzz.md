# CodeWars Python Solutions

---

## Fizz Buzz


Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1 (in C#, N might be less then 1).

- C# ONLY: If N is smaller then or equal to 0, throw an ArgumentOutOfRangeException!

Replace certain values however if any of the following conditions are met:

- If the value is a multiple of 3: use the value `'Fizz'` instead
- If the value is a multiple of 5: use the value `'Buzz'` instead
- If the value is a multiple of 3 & 5: use the value `'FizzBuzz'` instead

C# method calling example:

```
string[] result = FizzBuzz.GetFizzBuzzArray(3); // => [ "1", "2", "Fizz" ]
```

---

### Given Code


```python
def fizzbuzz(n):
    pass
```

---

### Solution


```python
def fizzbuzz(n):
    arr = []
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                arr.append("FizzBuzz")
            else:
                arr.append("Fizz")
        elif i % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(i)
    return arr
```

---


[See on CodeWars.com](https://www.codewars.com/kata/5300901726d12b80e8000498/)
