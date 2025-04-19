# Recursion:-

import sys
print(sys.getrecursionlimit())    #print(sys.getrecursionlimit()) ye line Python mein recursion limit ko print karti hai — 
#yani maximum number of times koi function apne aap ko recursively call kar sakta hai before Python error de de.
print(sys.setrecursionlimit(1900)) #print(sys.setrecursionlimit(1900)) ye line recursion limit ko 1900 set karne ki koshish karti hai, 

i=0
def demo():
    global i #Global Keyword
    i+=1
    print("Hello",i)
    demo() # Run Only 1000 time 

demo()