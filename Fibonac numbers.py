#Implement a program that prints Fibonacci series up to a given number.

num = int(input('Enter the number: '))

def fibonacci(num):
    a=0
    b=1
    print(a,end=' ')
    for i in range(num):
          
        print(b,end=' ')  
        a,b=b,a+b
        
fibonacci(num)