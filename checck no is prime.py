# Write a program to check if a number is prime.
def prime(num):
    count = 0
    if num < 2:
        return print('it\'s not Prime number')
        
    else:
        for i in range(2,int(num**0.5)+1):
            num%i == 0
            count+=1
            break
        
    if count==0:
        return print('prime number')
    else:
        return print(' not prime number')

num = int(input('Enter the number: '))
prime(num)