

#Is the string uppercase? v2

inp = "676@#"

def is_uppercase(inp):

    k = 0
    for i in inp:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            k = k + 1
    if k == 0:
        return True
    elif inp.isupper():
        return True
    else:
        return False

print(inp, is_uppercase(inp))



#Remove the time ver2

long_date = 'Sunday March 2, 8pm'

def shorten_to_date(long_date):
    p1, sep, tail = long_date.partition(',')
    return p1

print(shorten_to_date(long_date))

#Remove the time

long_date = 'Monday February 2, 8pm'

def shorten_to_date(long_date):

    sh_date = []
    i = 0

    while long_date[i] != ",":
        sh_date.append(long_date[i])
        i = i + 1

    return("".join(sh_date))

print(shorten_to_date(long_date))

#Sort My Textbooks

textbooks = ['Algebra', 'Geometry', 'english', 'history']

def sorter(textbooks):
    return sorted(textbooks,key=str.lower)
#,key=str.lower

print(sorter(textbooks))


#Is the string uppercase?

inp = "11YY2FA"

def is_uppercase(inp):

    k = 0
    for i in inp:
        if (('a' <= i <= 'z') or ('A' <= i <= 'Z')) != True:
            k = k + 1
        elif i.isupper():
            k = k + 1
    
    return (True if k == len(inp) else False)

print(is_uppercase(inp))
