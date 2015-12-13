# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are made up of different values generally of the same type. Items can be added and removed from a list and even modified within. Lists have a length and the values of the items within the list can be called with indexes. Similarly tuples have a length and their items are assigned to an index in the tuple. However once created a tuple cannot be modified. Because of this, tuples would work best as keys in dictionnaries since we would not want keys that could be modified.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Unlike lists, sets are unordered collections of unique elements. They do not support indexing, slicing or sequence-like behavior. Sets cannot contain mutable elements such as lists and dictionnaries but can contain immutable collections such as tuples.
>>> a = [1,3,2,4,3,5];
>>> list(a) > ([1,3,2,4,3,5])
>>> set(a) > ([1,3,2,4,5])
>>> Finding values in sets is faster because the location of the value is "set" and there is only one unique element. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is an anonymous function which means it was not initially declared as a function in the code but it will be used as one. The `lambda` key word is used to create an anonymous function.

>> * lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.

>> * an anonymous function cannot be a direct call to print because lambda requires an expression

>> * lambda function have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.

>> Syntax: 

>> `lambda [arg1, [arg2, ..., argN]]:expression` 

>> `sum = lambda arg1, arg2: arg1 + arg2`

>> `sum(10,20)
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is a concept used to construct lists in a very natural, easy way, like a mathematician is used to.

>> `s = [x**2 for x in range(10)]`

>> `v = [2**i for i in range(13)]`

>> `m = [x for x in s if x%2 == 0]`

>> List comprehensions can be nested in each other. They can contain any type of element, including strings, nested lists and functions. 

>> ex: the following works on a list of strings and produces a list of lists. Each of the sublists contains two strings and an integer. 

>> `words = "The quick brown fox jumps over the lazy dog".split()`

>> `stuff = [[w.upper(),w.lower(),len(w)] for w in words]`

>> In this case, it can also be done with map and a lumbda function as so: 

>> `stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)`

>> There are cases when one cannot use map() and have to use list comprhension instead, or vice-versa. Generally speaking, list comprehensions are faster with a lambda function whereas map is faster when one doesn't have to declare a lambda function.

>> **map()** : applies a function to every member of an iterable and returns the result. One can pass a lambda or any other function

>> **filter()**: takes a function returning TRUE or FALSE and applies it to a sequence, returning a list of only those members of the sequence for which the function returned TRUE.

```
#list:
ls = [x**2 for x in range(10) if x**2 > 10 and x**2 < 50]

Out: [16, 25, 36, 49]

#map:
def square(x):
  if x**2 > 10 and x**2 < 50:
    return x**2

mp = map(square, range(10))

Out: [None, None, None, None, 16, 25, 36, 49, None, None]

#filter:
flt = filter(lambda x: x**2 > 10 and x**2 < 50, range(10))

Out: [4, 5, 6, 7]
```

>> **set comprehensions**: `a = {x**2 for x in range(10)}`

>> **dictionary comprehensions** = `d = {x:x**2 for x in range(10)}`

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





