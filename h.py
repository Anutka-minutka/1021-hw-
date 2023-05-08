import random
a=round(random.uniform(1,100),2)
print(a)
try:
    if a != int:
        print('error')
except(ValueError):
    if a == 50:
        print('no error')
