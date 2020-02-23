# CodeWars Python Solutions

---

## HTML Generator

Another rewarding day in the fast-paced world of WebDev. Man, you love your job! But as with any job, somtimes things can get a little tedious. Part of the website you're working on has a very repetitive structure, and writing all the HTML by hand is a bore. Time to automate! You want to write some functions that will generate the HTML for you.

To organize your code, make of all your functions methods of a class called HTMLGen. Tag functions should be named after the tag of the element they create. Each function will take one argument, a string, which is the inner HTML of the element to be created. The functions will return the string for the appropriate HTML element.

For example,


```python
g = HTMLGen();
paragraph = g.p('Hello, World!')
block = g.div(paragraph)

# The following are now true
paragraph == '<p>Hello, World!</p>'
block == '<div><p>Hello, World!</p></div>'
```

Your `HTMLGen` class should have methods to create the following elements:

* a
* b
* p
* body
* div
* span
* title
* comment

Note: The comment method should wrap its argument with an HTML comment. It is the only method whose name does not match an HTML tag. So, g.comment(`'i am a comment')` must produce `<!--i am a comment-->`.


---

### Given Code


```python
class HTMLGen:
    pass
```

---

### Solution


```python
class HTMLGen:

    def a(self, strng):
          return "<a>{}</a>".format(strng)

    def p(self,strng):
          return "<p>{}</p>".format(strng)

    def b(self,strng):
          return "<b>{}</b>".format(strng)

    def body(self,strng):
          return "<body>{}</body>".format(strng)

    def div(self,strng):
          return "<div>{}</div>".format(strng)

    def span(self,strng):
          return "<span>{}</span>".format(strng)

    def title(self,strng):
          return "<title>{}</title>".format(strng)

    def comment(self,strng):
          return "<!--{}-->".format(strng)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/54eecc187f9142cc4600119e/)
