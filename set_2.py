spam = ['fat', 'dark', 'smart']

size, color, sense = 'lean', 'white', 'dummy'

print(size, color, sense)

size, color, sense = spam

print(size, color, sense)


print(spam.index('fat'))

#approach one to avoid error when the value doesnt exist
try:
    print(spam.index('dfdf'))
except ValueError:
    print(ValueError) #class ValueError

#approach two to avoid error when value doesnt exist
if ('dfdf' in spam):
    print(spam.index('dfdf'))
else:
    print('dfdf doesnt exists at ' + str(spam)) #dfdf doesnt exists at ['fat', 'dark', 'smart']


spam.append('busy')
print(spam)


#spam.append('brave', 'great') - doesnt work, it accepts only one argument
#print(spam)

spam.insert(1, 'generous')
print(spam)


spam = ['book', 'pen', 'pencil', 'box', 'another box',  'box']

spam.remove('box') #['book', 'pen', 'pencil', 'another box', 'box'] - removes the first appearing box

print(spam)


spam = [1, 5, 2, 8, 3, -4, 6]
spam.sort()
print(spam)

spam = ['elephant', 'monkey', 'hen', 'goat']
spam.sort(reverse=True)
print(spam)

spam = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']

spam.sort(key=str.lower)
print(spam)




