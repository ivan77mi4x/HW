#Double Char 

s = "hello world"

def double_char(s):
    s_dbl = []

    for i in s:
        s_dbl.append(i)
        s_dbl.append(i)

    return("".join(s_dbl))

print(double_char(s))


#Fix the loop!

animals = [ 'dog', 'cat', 'elephant', 'mouse' ]

def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list = list + (str(i + 1) + '. ' + animals[i] + '\n')
    return list
        
print(list_animals(animals))



#Grasshopper - Summation

def summation(num):
    pass # Code here
    sum = 0
    for i in range(1,num+1):
        sum = sum + i
    return(sum)

print(summation(4))
