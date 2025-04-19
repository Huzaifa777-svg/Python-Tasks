# Question:
# Given the following list:

# python
# Copy
# Edit
# my_list = [1, 2, 7, 5, 4]
# Part (a): Use indexing to replace the first element of the list with "apple".
# Part (b): Print the modified list.
# Part (c): What will be the output of this code?
"""list=[1,2,7,5,4]
list[0]="apple"
print(list)"""

#print list Indexing
"""list=[1,2,7,5,4]
print(list[3])"""

# last list add
"""list=[1,2,7,5,4]
list.append(6)
print(list)
"""
# index number 
"""list=[1,2,7,5,4]
list.remove(2)
print(list)
"""
# SORT
"""list=[1,2,7,5,4]       
list.sort()
print(list)
"""

# Last element 
"""list=[1,2,7,5,4]
print(list[-1])
"""
"""# last remove
list=[1,2,7,5,4]
list.pop()
print(list)
"""
# list insert
"""list=[1,2,7,5,4]
list.insert(2,"Graps")
print(list)
"""

# reverse
"""list=[1,2,7,5,4]
list.reverse()
print(list)
"""

# copy list
"""list=[1,2,7,5,4]
copy_list=list.copy()
print(copy_list)
"""
# deepcopy concept
"""import copy
# use nested list
orignal=[[1,2,3],["A","b","c"]]
print(orignal)
copyc=copy.deepcopy(orignal)
copyc[0][1]=20
print(copyc)"""

#search index
"""list=[1,2,7,5,4]
list.index(2)
print(list)"""


#delete index num
"""list=[1,2,7,5,4]
del list[3]
print(list)
"""

# concatinate 2 list
"""list_1=[20.9,3.0,12,7]
print(list,list_1)"""

#index ki 
"""list=[1,2,7,5,4]
length=len(list)
print(length)"""

# Write a Python program to calculate the sum of all even numbers in the given list:
# number=[2,5,4,8,7,1,9,10]
''''
number=[2,5,4,8,7,1,9,10]
sum=0
for numb in number:
    if numb%2==0:   
     sum+=numb
print("The Sum of even number is: ",sum)'''

# range:
"""p=list(range(100))
print(p)
"""
#start end:
"""p=list(range(2,9))
print(p)
step:
p=list(range(2,80,2))
print(p)

"""
# slice a list:
"""num=[1,2,3,4,5,6]
p=num[2:4]
print(p)
"""
# list comperision
"""
list=[j for j in range(9) if(2<9)]
new_list = [expression for item in iterable if condition]

print(list)"""
