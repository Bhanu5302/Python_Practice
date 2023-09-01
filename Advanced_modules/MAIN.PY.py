
'''
fgh=open('bhanu.txt')
count=0

for line in fgh:
    # print(line)
    for i in line:
        count=count+1

print(count)
'''

number=input("Enter number: ")
def factorial(num):
    for x in range(num):
        op=num*(num-1)
        num=num-1
    return op
output = factorial(10)
print(output)