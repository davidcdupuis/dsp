# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
import re

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        print("Number of donuts: " + str(count))
    else:
        print("Number of donuts: many")

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) > 2:
        print(s[0] + s[1] + s[len(s)-2] + s[len(s)-1])
    else:
        print('')

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    char = s[0]
    result = char
    for i in range(1, len(s)):
        if char == s[i]:
            result += '*'
        else:
            result += s[i]
    print(result)

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    result = b[0] + b[1]
    for i in range(2,len(a)):
        result += a[i]
    result += ' ' + a[0]  + a[1]
    for i in range(2,len(b)):
        result += b[i]
    print(result)

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    word = ''
    for i in range(0,len(s)):
        word += s[i]

    if len(s) >= 3:
        end = ''
        for i in range(len(s)-3,len(s)):
            end += s[i]
        if end == 'ing':
            word += 'ly'
        else:
            word += 'ing'
        print(word)
    else:
        print(word)

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    print(str(re.sub('not[\s\w]*bad','good',s)))

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    if len(a) % 2 == 0:
        a1 = a[:int(len(a)/2):1]
        a2 = a[int(len(a)/2):len(a):1]
    else:
        a1 = a[:int(len(a)/2+1):1]
        a2 = a[int(len(a)/2+1):len(a):1]

    if len(b) % 2 == 0:
        b1 = b[:int(len(b)/2):1]
        b2 = b[int(len(b)/2):len(b):1]
    else:
        b1 = b[:int(len(b)/2+1):1]
        b2 = b[int(len(b)/2+1):len(b):1]

    print(a1 + b1 + a2 + b2)

print("\nDonuts: ")
donuts(4)
donuts(9)
donuts(10)
donuts(40)

print("\nBoth ends: ")
both_ends('spring')
both_ends('Hello')
both_ends('a')
both_ends('xyz')

print("\nFix Start:")
fix_start('babble')
fix_start('aardvark')
fix_start('google')
fix_start('donut')

print("\nMix Up:")
mix_up('mix', 'pod')
mix_up('dog', 'dinner')
mix_up('gnash', 'sport')
mix_up('pezzy', 'firm')

print("\nVerbing:")
verbing('hail')
verbing('swiming')
verbing('do')

print("\nNot Bad:")
not_bad('This movie is not so bad')
not_bad('This dinner is not that bad!')
not_bad('This tea is not hot')
not_bad("It's bad yet not")

print("\nFront Back:")
front_back('abcd', 'xy')
front_back('abcde', 'xyz')
front_back('Kitten', 'Donut')
