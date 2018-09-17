import copy

spam = ['a', 'list', 'is', 'mutable', ['this', 'is' 'another', 'list']]

bread = spam;

bread.append('new')

print(spam)

bread_copy = spam.copy()

bread_copy.insert(1, 'good')

print(spam) #doesnt change the original list

print(bread_copy)

