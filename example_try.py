print('Which version of python you have ?')
version = input()
try:
    if (int(version)>2):
        print('Its quite updated one!')
    else:
        print('Its not an updated one!')
except ValueError:
    print('Please enter a valid value')
