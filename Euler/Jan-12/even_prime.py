import sys
def fibonacci(n): 
        sum1 = 0 
        sum2 = 1 
        sum3 = 0 
        present = 0 
        arr = []
        for i in range(0,n): 
            sum3 = sum1 + sum2 
            sum1 = sum2 
            sum2 = sum3 
            arr.append(sum2)
            if sum2 % 2==0 and max(arr)<n: 
                present = present + sum2 
             
        print(present) 
                        

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fibonacci(n)