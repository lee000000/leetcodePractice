# coding: utf-8
"""
Write a program that outputs the string representation 
of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead 
of the number and for the multiples of five output “Buzz".
For numbers which are multiples of both three and five output 
“FizzBuzz”.
"""

def fizz_buzz(n):
    lst = []
    if n == 1:
        return ["1"]
    i = 1
    while i < n + 1: 
        if i == 0:
            continue
        if (i % 3 == 0 and i % 5 != 0):
            lst.append("Fizz")
        elif ( i % 5 == 0 and i % 3 != 0):
            lst.append("Buzz")
        elif (i % 15 == 0):
            print(i)
            lst.append("FizzBuzz")
        else:
            lst.append( str(i))
        i += 1
    return lst

if __name__ == "__main__":
    lst = fizz_buzz(100)
    print(lst)
