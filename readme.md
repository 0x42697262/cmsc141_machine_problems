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



# Sources Used
- MP2 Primer
- https://regexr.com/
- https://stackoverflow.com/questions/38579725/return-string-with-first-match-for-a-regex-handling-case-where-there-is-no-matc
- https://www.youtube.com/watch?v=rsxjCkvYoAw
- https://www.youtube.com/watch?v=7nENzjQTxCc
- https://stackoverflow.com/questions/12643009/regular-expression-for-floating-point-numbers