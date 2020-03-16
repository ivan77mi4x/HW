#сортувати цифри числа

number = 5896
ascending = "".join(sorted(str(number)))
print (ascending)


#записати число в зворотньому порядку

num = 5896
text = ''.join(reversed(str(num)))
#number = number[::-1]
print(text)


#добуток чисел заданого числа v2

number = 135
dob = 1

for i in str(number):
    dob = dob * int(i)

print("dob v2:", dob)


#добуток чисел заданого числа

number = 123
mul = 1
while (number>0):
    rem = number%10
    mul = mul*rem
    number = number//10
print (mul)


#замінити задані значення 

zen = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
zen = zen.replace("i", "&")
print (zen)


#порахувати кількість заданих слів у тексті

zen = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
substring_1 = "better"
count_1 = zen.count(substring_1)
substring_2 = "never"
count_2 = zen.count(substring_2)
substring_3 = "is"
count_3 = zen.count(substring_3)

print ("The word 'better' is used:", count_1, "times")
print ("The word 'never' is used:", count_2, "times")
print ("The word 'is' is used:", count_3, "times")

#вивести текст стрічки у верхньому регістрі

zen = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.

If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
print (zen.upper())

