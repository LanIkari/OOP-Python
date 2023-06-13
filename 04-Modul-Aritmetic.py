#Program 04
# Sum of two numbers, whit validation of null values
def sum(a,b):
    if a!=None and b!=None:    
        c=a+b
    else:
        print("Ingrese ambos valores")
        c=0
    return c

#We can specifi the numbers in the function, if we don't, the default values are 0 and 1.
def rest(a=0, b=1):
    return a-b