from django.test import TestCase

# Create your tests here.



def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


print(factorial(5))