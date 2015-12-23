# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    count = 0 
    for word in words:
        if len(word) >= 2 and word[0] == word[len(word)-1]:
            count += 1
    print(str(count))


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    words.sort()
    for word in words:
        if word[0] == 'x':
            words.pop(word.index(word))
            words.insert(0,word)
    print(words)


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    #other option: sorted(data, key=lambda tup: tup[1])
    tuples.sort(key=lambda tup: tup[len(tup)-1])#should be on last element in tuple
    print(tuples)


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    a =[]
    if nums: 
        a.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                a.append(nums[i])
    print(a)


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    lst = []

    if len(list1) > len(list2):
        l1 = list1
        l2 = list2
    else:
        l1 = list2
        l2 = list1

    a = 0

    for i in l1:
        if a < len(l2):
            while a < len(l2):
                if i < l2[a]:
                    lst.append(i)
                    break
                else:
                    lst.append(l2[a])
                    a += 1
                    if a == len(l2):
                        lst.append(i)
        else:
            lst.append(i)

    print(lst)

print("\nMatch ends:")
match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
match_ends(['', 'x', 'xy', 'xyx', 'xx'])
match_ends(['aaa', 'be', 'abc', 'hello'])

print("\nFront X:")
front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])

print("\nSort Last:")
sort_last([(1, 3), (3, 2), (2, 1)])
sort_last([(2, 3), (1, 2), (3, 1)])
sort_last([(1, 7), (1, 3), (3, 2, 5), (2, 2)]) # changed (3,4,5) to (3,2,5) to make sure sorting was done on last element

print("\nRemove adjacents:")
remove_adjacent([1, 2, 2, 3])
remove_adjacent([2, 2, 3, 3, 3])
remove_adjacent([3, 2, 3, 3, 3])
remove_adjacent([])

print("\nLinear merge:")
linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])