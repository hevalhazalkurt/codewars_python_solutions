# CodeWars Python Solutions

---

## Decode the Morse code

***Part of Series 1/3*** : This kata is part of a series on the Morse code. After you solve this kata, you may move to the next one.

In this kata you have to write a simple [Morse code](https://en.wikipedia.org/wiki/Morse_code) decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.

The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter `A` is coded as `·−`, letter `Q` is coded as `−−·−`, and digit `1` is coded as `·−−−−`. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message `HEY JUDE` in Morse code is `···· · −·−−   ·−−− ··− −·· ·`.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal [SOS](https://en.wikipedia.org/wiki/SOS) (that was first issued by Titanic), that is coded as `···−−−···`. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

```python
decodeMorse('.... . -.--   .--- ..- -.. .')
# should return "HEY JUDE"
```

NOTE: For coding purposes you have to use ASCII characters `.` and `-`, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

* Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: `MORSE_CODE['.--']`
* C#: MorseCode.Get(".--") (returns string)
* Elixir: `@morse_codes` variable (from `use MorseCode.Constants`). Ignore the unused variable warning for `morse_codes` because it's no longer used and kept only for old solutions.
* Elm: `MorseCodes.get : Dict String String`
* Haskell: `morseCodes ! ".--"` (Codes are in a `Map String String`)
* Java: `MorseCode.get(".--")`
* Kotlin: `MorseCode[".--"] ?: ""` or `MorseCode.getOrDefault(".--", "")`
* Rust: `MORSE_CODE`
* Scala: `morseCodes(".--")`
* Swift: `MorseCode[".--"] ?? ""` or `MorseCode[".--", default: ""]`
* C: provides parallel arrays, i.e. `morse[2] == "-.-"` for `ascii[2] == "C"`
* NASM: a table of pointers to the morsecodes, and a corresponding list of ascii symbols

All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.

Good luck!


---

### Given Code


```python
def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
```

---

### Solution


```python
def decodeMorse(morse_code):
    message = "".join([MORSE_CODE[i] if i in MORSE_CODE else " " for i in morse_code.split(" ")])
    return message.replace("  ", " ").strip()
```


---


[See on CodeWars.com](https://www.codewars.com/kata/54b724efac3d5402db00065e/)
