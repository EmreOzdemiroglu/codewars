import re

def disemvowel(string):
    vow = "aeiouAEIOU"
    for i in vow:
        string = re.sub(i, "", string)
    return string

print(disemvowel("This website is for losers LOL!"))

#others

"""
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

def disemvowel(string):
    return string.translate(None, 'aeiouAEIOU'

def disemvowel(str2handle):
    vowel_character = ["a", "A", "e", "E", "o", "O", "i", "I", "u", "U"]
    str2return = ""
    i = 0
    n = len(str2handle)
    while i < n:
        if not str2handle[i] in vowel_character:
            str2return += str2handle[i]
        i += 1
    return str2return

def disemvowel(string):
    return string.translate(None, 'aeiuoAEIOU')

import re

def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]", "", string)

import re

def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]", "", string)

def disemvowel(string):
        
    s = ""
    for c in string:
        if c.lower() not in "aeiou":
            s += c
    return s

def disemvowel(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for i in string:
        if i not in vowels:
            new_string+= i 
    return new_string

def disemvowel(string):
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    answer = ""
    for letter in string:
        if not letter in vowels:
            answer += letter
    return answer


def disemvowel(string):
    string = string.translate(None, "aAeEiIoOuU")
    return string

vowels = "aeieuo"
def disemvowel(string):
    i = 0
    while i < len(string) :
        if string[i] in vowels or string[i] in vowels.upper():
            string = string[:i] + string[i+1:]
            i -= 1
        i += 1
    return string

def disemvowel(string):
    return string.translate(None, "AEIOUaeiou")

import re
def disemvowel(string):
    return re.sub(r'(?i)[aeiou]','',string)


def disemvowel(string):
    result = ""
    for i in range(0, len(string)):
        c = string[i]
        if c == 'A':
            continue
        if c == 'E':
            continue
        if c == 'I':
            continue
        if c == 'O':
            continue
        if c == 'U':
            continue
        if c == 'a':
            continue
        if c == 'e':
            continue
        if c == 'i':
            continue
        if c == 'o':
            continue
        if c == 'u':
            continue
        result += c
    return result

def disemvowel(string):
  return "".join([c for c in string if c not in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']])


def disemvowel(string):
    v = 'aeiouAEIOU'
    return filter(lambda x: x not in v, string)

def removeAll(string, letters):
    for l in letters:
        string = string.replace(l, "")
    return string

def disemvowel(string):
    return removeAll(string, "aeiouAIEOU")

import re

def disemvowel(string):
    wordList = re.findall('([^aeiouAEIOU]+)*',string)
    return  "".join([word for word in wordList ])

def disemvowel(string):
    return string.translate({ord(i):None for i in 'aeiouAEIOU'})

def disemvowel(string):
    return string.translate(None, 'aAeEuUoOiI')

def disemvowel(s):

    L=["a","e","i","o","u"]
    L1=[]
    for i in s:
        if i.lower() not in L:
            L1.append(i)
    return "".join(L1)

def disemvowel(string):
    return string.translate(None, 'aAeEuUoOiI')

def disemvowel(string):
    set = 'aieuoIOUEA'
    liste = string.translate(None, set)
    return liste




"""
