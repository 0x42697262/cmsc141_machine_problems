i'm too lazy to make one for now. future me can probably handle it without checking docs, i think - i regret saying this as of thursday of may 2022


# Machine Problem 1: Ready get SET!

## Files Used

- ~~[mp1.cpp](https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1.cpp) (switched to cpp because why not for the first time python is hard)~~
- ~~[mp1.py](https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1.py) (the main driver code)~~
- [mpa1.in](https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mpa1.in) (input test file)
- [mp1_v2.py](https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1_v2.py) (went back to python, i'm giving up on this sets. i'll just string everything on a dictionary.)

---

## General Description

For this MP, you are to implement the set data structure.
The set data structure is a container that stores unique elements in no particular order which should
allow for fast access. For this MP, implement the following operations for the set data structure:
1. insert
2. remove
3. subset
4. union
5. intersection
6. difference
7. power set

## Input File

The input file (named mpa2.in) will contain a number of lines. The first line is the number of test
cases. Each test case will contain a series of lines as well. The first line will contain a number
representing what type of sets are to be created (exactly two sets will be created for each test case).
The following are the different types:
1. int
2. double
3. char
4. string
5. set
6. object


---

**Completed Structures**

- [x] insert
- [x] remove
- [x] subset
- [x] union
- [x] intersection
- [x] difference
- [ ] powerset

**Completed Types**

- [x] int
- [x] double
- [x] char
- [x] string
- [ ] set
- [ ] object

---

## InputFileHander
- _filename: filename .-.
- _lines: a list where we store the lines of the file

```python
start_reading()
```
Reads the file and appends each line to _lines variable.

```python
_print()
```
Prints each line of the file from _lines.

```python
_get_line(arg)
```
Return specific line based on the argument int.

```python
_get_size()
```
Return size of _lines.

```python
get_me()
```
Returns the list of _lines.


## Set
i am too lazy to document ahhhhhhhhhhhhhhhhhhhhhhh



---

# TL;DR How do I use this code

wtf should i just recode everything from scratch?? i don't understand this anymore.


----

# Machine Problem 2: Paparazzi, Grammar Nazi

## Files Used
- [mp2.py](https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp2.py)

## General Description
Before a compiler converts a source file into a machine readable code, the syntax of the source file is checked first. For this MP, you are going to simulate this syntax checking for a source code written in c.

**Scope**

The MP will require you to check the syntax of the following expressions in c:
- variable declaration
- function declaration
  
Multiple declarations, including those with initializations, are in scope. This also means that identifiers have to be checked. They should follow the naming rule of c, i.e. they can start with '_' or any letter from the English alphabet, followed by 0 or more alpha-numeric characters, including the '_'.

**Variable declaration**

The MP will stick with primitive types. The types are:

- int
- char
- float
- double

## messy code, no documentation :D

# Machine Problem 3: Paparazzi, Grammar Nazi Version 2.0
Basically the same as MP2

# Machine Problem 3: Smiling must me a Regular Expression
## Files Used
- [mp3_regexpr.py](https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp3_regexpr.py)
## General Description

Given a regular expression, determine whether certain strings are generated by it.

## Scope

The MP will require you to apply the different operators used in regular expressions. This includes the following:

- union
- concatenation
- Kleene star

## union

The symbol ‘+’ will be used to denote union or “OR”. Single symbols or concatenated strings may surround it.

- a + b

- e+a + b

- aba + bba + e

## concatenation

No symbol will be used for concatenation. Symbols that are beside each other are considered to have been concatenated. And possibly enclosed with parentheses

- aaabbb
- ab
- bbbbbb
- a(a+b)a

## Kleene star

The use of the Kleene is limited to single symbols and grouped/concatenated symbols. It will not be used with “OR-ed” symbols or strings. And “starring” starred grouped/concatenated symbols is not in scope as well.

- aaa\*
- a*bb\*
- (ab)\*
- ((ab)(ba)\*)\*  or ((aba)\*(bab)\*)\* - FORMS LIKE THIS ARE NOT IN SCOPE
- (a+b)\* or (ab+ ba)\* - FORMS LIKE THIS ARE NOT IN SCOPE AS WELL

 
## Input

The input file consists of a number of lines. The first line contains the number of test cases.  The following lines contain the test cases. Each test case consists of the regular expression, followed by a number representing the number of strings that need to be verified or tested (whether the regular expression generates the string (yes) or not (no) ). What follows next are the actual strings to be tested.

## Code
The function `Interpreter()` takes input and returns a dictionary of test cases.

Example returned dictionary with 3 test cases:
```python
{
    0: ["ab*",   ["aaaa", "ababba", "abab"]],
    1: ["ab+ba", ["abab", "ba"]],
    2: ["abab",  ["ba", "baba", "abababab", "abab", "a"]]
}
```
The key serves as an index of some sort while the value of the key is a list. The first index of the list always contains the regular expression while the second index are the strings.

The class `RegExpr` initializes with the input of cases taken from the second index of the returned data dictionary from the `Interpreter()`. It sorts the first index as its regular expression while the second index list are the strings.

```python
self._match = []
self._expr = case[0].replace('+', '|').replace(' ', '')
self._strings = case[1]
```
- `self._match` - matching result of the iterated string
- `self._expr` - the input regular expression (first index of the taken list)
- `self._strings` - input of strings that are to be tested by the regular expression input (second index of the taken list)

The function `test_a_string` iterates through the strings list and use Python's builtin regex module to check if the regular expression input satisfies the string. This then appends the matching result to the class variable `self._match`.

# Sources Used
- MP2 Primer
- https://regexr.com/
- https://stackoverflow.com/questions/38579725/return-string-with-first-match-for-a-regex-handling-case-where-there-is-no-matc
- https://www.youtube.com/watch?v=rsxjCkvYoAw
- https://www.youtube.com/watch?v=7nENzjQTxCc
- https://stackoverflow.com/questions/12643009/regular-expression-for-floating-point-numbers