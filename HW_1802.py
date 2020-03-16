#fibo

def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

n=int(input("Input your number for Fibonachi sequence: "))

for i in range(1,n+1):
    print(fib(i))



#Multiples of 3 or 5 - 2

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


#Multiples of 3 or 5

number = 11
print(range(number))

def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return(sum)

print(solution(number))



#Reverse List Order

l=[1,2,3,4,5]

def reverse_list(l):

    l_out = []
    for i in range(len(l)):
        l_out.append(l[len(l)-1-i])

    return(l_out)

print(reverse_list(l))


#Count of positives / sum of negatives - 2

arr = [10,12,19,-7,-8]

def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    else:
        a = len([x for x in arr if x>0])
        b = sum([x for x in arr if x<0])
        return [a,b]

print(count_positives_sum_negatives(arr))



#Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
    kp = 0
    sum_n = 0
    ar_out = []

    for i in range(len(arr)):
        if arr[i] > 0:
            kp = kp + 1
        else:
            sum_n = sum_n + arr[i]

    if len(arr) != 0: 
        ar_out.append(kp)
        ar_out.append(sum_n)

    return(ar_out)
    
print(count_positives_sum_negatives([]))

