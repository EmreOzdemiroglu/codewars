def longest(s1,s2):
    f=""
    for s in s1:
        if not s in f:
            f+=s
    for s in s2:
        if not s in f:
            f+=s
    sortedd=sorted(f)
    sortedd="".join(sortedd)
    return sortedd


def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

def longest(s1, s2):
    # your code
    
    # Defining the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Concatenating the Two Given Strings
    s = s1 + s2
    
    # Declaring the Output Variable
    y = ""
    
    # Comparing whether a letter is in the string
    for x in alphabet:
      if x not in s:
        continue
      if x in s:
        y = y + x
        
    # returning the final output    
    return y


def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))

def longest(s1, s2):
    # your code
    distinct = set(s1+s2) # sets are distinct values! 
    distinctSorted = sorted(distinct) # turn into sorted list
    return ''.join(distinctSorted) # concatenate to string with 'join'



def longest(s1, s2):
    return ''.join(sorted(set(s1).union(s2)))

def longest(s1, s2):
    x=''
    y=sorted(s1+s2)
    
   
    
    for i in y:
      if i not in x:
        x += i
        
    return x # your code

def longest(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    return "".join(sorted(set1 | set2))
def longest(s1, s2):
    freq = {}
    for c in list(s1):
        freq[c] = freq.get(c, 0) + 1
    for c in list(s2):
        freq[c] = freq.get(c, 0) + 1
    l = sorted([c for c in list(freq.keys())])
    return ''.join(l)
import itertools
def longest(s1, s2):
    longest = ""
    for i in s1: 
        if i not in longest:
            longest += i
    for i in s2:
       if i not in longest:
            longest += i 
    return ''.join(sorted(longest))

def longest(s1, s2):
    results = []
    for records in s1:
        if records not in results:
            results.append(records)
    for records in s2:
        if records not in results:
            results.append(records)
    results = sorted(results)
    return "".join(results)

def longest(s1, s2):
    return "".join([x for x in "abcdefghijklmnopqrstuvwxyz" if x in s1+s2])

longest = lambda x,y: ''.join(sorted(set(x+y)))
def longest(s1, s2):
    new_string = set(s1 + s2)
    sort_string = sorted(new_string)
    return "".join(s for s in sort_string)
    
    # your code
def longest(s1, s2):
    letters_count = [0] * 26
    for letter in s1:
        letters_count[ord(letter) - 97] += 1
    for letter in s2:
        letters_count[ord(letter) - 97] += 1
    result = []
    for i in range(26):
        if letters_count[i] > 0:
            result.append(chr(i+97))
    return ''.join(result)

import string

def longest(s1, s2):
    
    comb = []
    alphabet = {}
    ind = 0
    
    for letter in s1:
        if letter in comb:
            pass
        else:
            comb.append(letter)
    
    for letters in s2:
        if letters in comb:
            pass
        else:
            comb.append(letters)
    
    lowerCase = list(string.ascii_lowercase)
    
    for letters in lowerCase:
        ind+=1
        alphabet[letters] = ind
    
    for x in range(len(comb)):
        for i in range(len(comb)-1):
            if alphabet[comb[i]] > alphabet[comb[i+1]]:
                comb[i], comb[i+1] = comb[i+1], comb[i]

    comb = ''.join(comb)
    
    return comb
