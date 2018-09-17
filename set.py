spam=['dog','cat','rat','snail']

for i in spam:
    print(i + ' chases ' + spam[1])

for i in range(len(spam)):
    if i+1 >= len(spam):
        j=0
    else:
        j=i+1

    print (spam[i] + ' chases ' + spam[j])

print(spam[:2]) #dog, cat

print(spam[2:3]) #rat, it starts from item:2 and go upto, but doesnt include item:3

print(spam[-1]) #snail: -2 refers to the last 2nd item

del spam[3]

print(spam) #['dog', 'cat', 'rat']

spam *= 3;

print(spam) #['dog', 'cat', 'rat', 'dog', 'cat', 'rat', 'dog', 'cat', 'rat']

theString = 'This is the string'

theString = list(theString)

print(theString)

theNum = 1234567890
try:
    print(list(theNum))
except TypeError:
    print('error TypeError')

f  = ['a', 'b', 'c']
print ('a' in f)

