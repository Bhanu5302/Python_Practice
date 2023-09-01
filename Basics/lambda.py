l1=[1,2,3,4,5,]
#------------------
add=lambda a,b:a+b
print(add(2,4))
#-------------------

#-----using map function & list-------
multilply=lambda a:a*3
output=map(multilply,l1)
print(list(output))