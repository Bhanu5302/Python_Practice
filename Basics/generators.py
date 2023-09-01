# yield keyword is used to return values multiple times from function
def f1():
    yield 1
    yield 2
    yield 3

result = f1()

#print next values in result
print(result.__next__())
print(result.__next__())
print(result.__next__())

#print all values in result using for loop
for value in result:
    print(value)