#assert 2+2==5, 'Думай краще'

#"""
#>>> 100/3
#6
#if __name__=='__main__':
   # import doctest
    #doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result