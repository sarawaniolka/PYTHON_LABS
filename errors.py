# import sys
#
# print("Hello")
# a = None
# sys.stdout.write('OK')
# sys.stderr.write('Error')

class MyError(Exception):
    pass

try:
    a = int(input("Provide a: "))
    b = 15
    c = b/a
    print('c: {}'.format(c))
    if c>10:
        raise MyError('c is greater than 10')
except ZeroDivisionError as de:
    print('I got zero division: {}'.format(de))
except ArithmeticError as de:
    print('I got arithmetic error: {}'.format(de))
except Exception as e:
    print('Got an exeption: {}'.format(e))
print('Final')

