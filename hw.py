import colorama

def first_function():
    pass
class Human:
    pass

cm=colorama
first=first_function
nick=Human

print(colorama.__name__)
print(cm.__name__)
print(first.__name__)
print(first_function.__name__)
print(Human.__name__)
print(nick.__name__)
print(__name__)

print(type(2))
print(type(2.1))
print(type(2==2))
print(type('hfd'))

into_list=[]
for method in dir(into_list):
    print(method)

into_dict={}
for method in dir(into_dict):
    print(method)


for method in dir():
    print(method)
