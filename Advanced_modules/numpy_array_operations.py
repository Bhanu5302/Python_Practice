import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,0],dtype='int64')
arr2=np.array(["bhanu","prakash","mamidi"])

#---------------array slicing-----------------------
print(arr[1:5]) # print values 1st index to 5th index
print(arr[4:]) # print 4th index to last index
print(arr[:4]) # print start index to 4th index value

#-----------------Data types-------------------------
print(arr.dtype)
print(arr2.dtype)

#---------------Copy arrays & view---------------
arr4=np.array([1,2,4,5,3,2,99])
arr5=arr4.copy()
arr6=arr4.view()
print(arr5)
print(arr6)

#---------------_Array shape_---------------------
arr7=np.array([[1,2,3,4],[5,6,7,8]])
print(f"shape of the array is: {arr7.shape}")

#---------creating 5D array using ndmin=5------
arr8=np.array([1,2,3,4,5,6],ndmin=5)
print(arr8)
print(arr8.shape)

#-----------Reshaping array-------------------
arr9=np.array([1,2,4,5,7,4,3,2,4,7,8,45])
arr10=arr9.reshape(3,4)  # 3 rows > each row 4 elements
print(f"reshaped array:{arr10}")
arr10=arr9.reshape(2,2,3)  # 2 Dimensions, 2 rows , 3 elements for each row
print(f"reshaped multidimension array: {arr10}")

#----------Iterations in array------------------
arr11=np.array([[1, 2, 3], [4, 5, 6]])

for x in arr11:   # for print each dimension
  print(x)

for x in arr11:   # for print each element in each array
    for y in x:
        print(y)
#-----------------------------------------------

#--------------Array concatenation--------------
arr12=np.array([[1,2,3],[2,4,2]])
arr13=np.array([[4,5,6],[5,5,3]])
arr14=np.concatenate((arr12,arr13))
arr15=np.concatenate((arr12,arr13), axis=1)
print(arr14)
print(arr15)
#-----------------------------------------------

#-------------Array Splitting--------------------
arr16=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr17=np.array_split(arr16,2)
print(arr17)
print(arr17[0])
print(arr17[1])


#--------------Array search---------------------
arr18=np.array([1,3,4,2,2,3,4,5])
print(np.where(arr18==4))
print(np.where(arr18%2 == 0))

#--------------Soring an array-----------------
print(np.sort(arr18))

#--------------


