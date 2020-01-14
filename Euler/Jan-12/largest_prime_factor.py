import sys
import math
def largest(num):
    n = num
    arr = []
    for number in range(2,n+1):
        for i in range(2,number):
            if number%i==0:
                break
        else:
            arr.append(number)
    
    x = len(arr)
    sum = 0
    for k in range(0,x):
        if num%arr[k]==0 and arr[k]>sum:
            sum = arr[k]
        
    print (sum)        
    

t = int(input())
for a0 in range(t):
    numb = int(input())
    largest(numb)

