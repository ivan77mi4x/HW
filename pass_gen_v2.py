import random

alph = "abcdefghijklmnopqrstuvwxyz"
alphup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dig = "0123456789"
ss = "~!@#$%^&*()_+"

l = [alph, alphup, dig, ss]
passw = []

len_p = int(input("введіть довжину паролю: "))
numb_passw = int(input("введіть кількість паролів: "))
print("")

while True:

  alph_b = int(input("маленькі букви присутні, 0 або 1: "))
  alphup_b = int(input("великі букви присутні, 0 або 1: "))
  dig_b = int(input("цифри присутні, 0 або 1:  "))
  ss_b =int(input("спецсимволи присутні, 0 або 1: "))
  print("")

  if alph_b == 0 and alphup_b == 0 and dig_b == 0 and ss_b == 0:
    print("не вибрано жодного типу даних")
  else:
      break
  
if alph_b == 0:
  l.remove(alph)
if alphup_b == 0:
  l.remove(alphup)
if dig_b == 0:
  l.remove(dig)
if ss_b == 0:
  l.remove(ss)

num_types = alph_b + alphup_b + dig_b + ss_b
k = 0

for j in range(1,numb_passw + 1):
    for i in range(len_p):
        passw.append(random.choice(l[k]))
        k = k + 1
        if k == num_types:
            k = 0
    random.shuffle(passw)
    print("password {}:".format(j),''.join(passw))
    passw = []
