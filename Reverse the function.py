#Create a function to reverse a string without using built-in methods.
def rev_string(string):
    rev = ''
    for i in string:
        rev = i + rev
    return rev
string = str(input('Enter the string: '))
print(rev_string(string))