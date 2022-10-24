"""
11. A while loop with errors

Assume a program has been written for the task of adding all integers I = 1, 2, ...10:
Some_number = 0
i = 1
While i < 11
Some_number += 1
Print some_number
a. Identify the errors in the program by only reading the code.
* Ans: It will cause a infinite loop. *

b. Write a new version of the program with the errors corrected. Run this program and
confirm that it gives the correct output.

"""

some_number = 0

for i in range(1, 11):
    some_number += i
print(some_number)