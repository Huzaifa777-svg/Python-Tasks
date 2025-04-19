#01) how to find the length ?

'''a={1,3,234,5,6,7,8}
print(len(a))'''


# Question 02) how to create an empty set?
'''a=set()
print(a)
print(type(a))'''

# qustion 4) Find the common elements between sets X and Y using intersection() ?

'''x={1,2,3,4,6,8,78,90}
y={23,45,23,12,1,3,4}
print(x.intersection(y))'''
# question 5) Use the union() method to create a set that contains all elements from both A and B ?

'''a={1,2,3,456,67,789}
b={89,34,1,4,67,3}
print(a.union(b))'''

# question 066) What elements are in the odd set but not in the even set? Use difference()?

'''
odd={1,2,3,4,5,7,89}
even={90,6,53,23,2,1,4}
print(odd.difference(even))'''

# question 07) Which elements are in either set1 or set2 but not in both? Use symmetric difference()?

# a={'Huzaifa'}
# a.add('charlie')
# print(a)
#question 08:8) Add the name "Charlie" to the set using add().

'''a={1,4,5,6,7,8,4}
b={1,10,23,4,6,7,90}
print(a.symmetric_difference(b))'''

#question 09
'''
a={1,2,5,6,7,8}
b=a.copy()
b.add(40)
print("A",a)
print("B",b)'''

#question 3
'''a={1,2,3,4,5,78,8,9}
b={12,24,4.5,66,2}
c={10,20,1,23,45,2}
print(a.union(b,c))'''