def devide(num):
    return 43//num

print(devide(9))
try:
    print(devide(0))
except ZeroDivisionError:
    print('error')
