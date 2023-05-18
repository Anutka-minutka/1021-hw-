#print('ya nadiysa v mene vuyde')
try:
    print('start')
    print(6/2)
    print('no error')
except ,NameError):
    print('We have an error')
print('code after capsule')

def checker(var_1):
    if type(var_1)!=int:
        raise TypeError(f"Sorry, we can't work with {type(var_1)}, "f"we need class int")
    else:
        return var_1
first_var=10
checker(first_var)