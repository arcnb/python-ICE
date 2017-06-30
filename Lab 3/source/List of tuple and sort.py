tupp=[]
for inx in range(0,3):
    X=str(input('Enter a single tuple: '))
    Y=tuple(map(int,X.split(',')))
    tupp.append(Y)
print('list of tuples is: ')
print(tupp)
Z= sorted(tupp, key=lambda x: x[-1])
print('Sorted List is: ')
print(Z)