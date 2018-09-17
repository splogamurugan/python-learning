spam_tuple = ('this', 'that', 'there')

for i in spam_tuple:
    print i
try:
    spam_tuple[0] = 'This'
except:
    print('error')
