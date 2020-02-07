# CodeWars Python Solutions

---

## The Wide-Mouthed frog!

The wide mouth frog is particularly interested in the eating habits of other creatures.

He just can't stop asking the creatures he encounters what they like to eat. But then he meet the alligator who just LOVES to eat wide-mouthed frogs!

When he meets the alligator, it then makes a tiny mouth.

Your goal in this kata is to create complete the `mouth_size` method this method take one argument `animal` which corresponds to the animal encountered by frog. If this one is an `alligator` (case insensitive) return `small` otherwise return `wide`.

---

### Given Code


```python
def mouth_size(animal):
  # code here
```

---

### Solution


```python
def mouth_size(animal):
  return "small" if animal.lower() == "alligator" else "wide"
```


---


[See on CodeWars.com](https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89)
