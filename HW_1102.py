#https://www.codewars.com/kata/is-this-my-tail/train/python

def correct_tail(body, tail):
     return tail == body[-1]

print(correct_tail("fox", "x"))


#https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python

def count_sheeps(sheep):
  # TODO May the force be with you
  return(sheep.count(True))

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, False,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

print(count_sheeps(array1))
    

#https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no

def bool_to_words(boolean):
    return("Yes" if boolean else "No")

print("bool_to_words:", bool_to_words(1))



#https://www.codewars.com/kata/are-you-playing-banjo

def areYouPlayingBanjo(name):
    return((name + " plays banjo") if name[0].lower() == "r" else
           (name + " does not play banjo"))

print(areYouPlayingBanjo("Rich"))


#https://www.codewars.com/kata/will-there-be-enough-space/train/python

def enough(cap, on, wait):
    return( "eno_spa" if (on + wait) <= cap else ("can't take:", on + wait - cap))

print(enough(10,4,6))


#https://www.codewars.com/kata/will-you-make-it

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return(True if distance_to_pump <= mpg * fuel_left else False)

print(zero_fuel(50, 40, 1.5))
