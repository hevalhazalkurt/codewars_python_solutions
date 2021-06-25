# CodeWars Python Solutions

---

## Easy Balance Checking

You are given a (small) check book as a - sometimes - cluttered (by non-alphanumeric characters) string:

```
"1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10"
```

The first line shows the original balance. Each other line (when not blank) gives information: check number, category, check amount. (Input form may change depending on the language).

First you have to clean the lines keeping only letters, digits, dots and spaces.

Then return a report as a string (underscores show spaces -- don't put them in your solution. They are there so you can see them and how many of them you need to have):

```
"Original_Balance:_1000.00
125_Market_125.45_Balance_874.55
126_Hardware_34.95_Balance_839.60
127_Video_7.45_Balance_832.15
128_Book_14.32_Balance_817.83
129_Gasoline_16.10_Balance_801.73
Total_expense__198.27
Average_expense__39.65"
```

On each line of the report you have to add the new balance and then in the last two lines the total expense and the average expense. So as not to have a too long result string we don't ask for a properly formatted result.

**Notes**

* See input examples in Sample Tests.
* It may happen that one (or more) line(s) is (are) blank.
* Round to 2 decimals your results.
* The line separator of results may depend on the language `\n` or `\r\n`. See examples in the "Sample tests".
* R language: Don't use R's base function "mean()" that could give results slightly different from expected ones.

---

### Given Code


```python
def balance(book):
    pass
```

---

### Solution


```python
def balance(book):
    chars = "!=:;-_+^/(){}?*'%&@,;$#€"

    for c in chars:
        if c in book:
            book = book.replace(c, "")

    lines = book.split("\n")
    balance, total, expense, last = None, 0, 0, []

    for e,i in enumerate(lines):
        if len(i) == 0:
            continue
        elif e == 0:
            balance = float(i)
            last.append("Original Balance: {:.2f}".format(balance))
        else:
            data = i.split(" ")
            amount = float(data[2])
            total += amount
            last.append("{} {} {:.2f} Balance {:.2f}".format(data[0], data[1], float(data[2]), round(balance-amount,2)))
            balance -= amount
            expense += 1

    average = round(total/expense, 2)
    last.append("Total expense  {:.2f}".format(round(total,2)))
    last.append("Average expense  {:.2f}".format(average))
    return "\r\n".join(last)
```


---


[See on CodeWars.com](https://www.codewars.com/kata/59d727d40e8c9dd2dd00009f/)
