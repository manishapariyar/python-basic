# import keyword
# print(keyword.kwlist)
# # input("press enter to continue")
# name = input("what is your name? ")
# print("hello " + name)
# age = int(input("Enter a number: "))

# if age >= 18:
#     print(f" {name}! your are eligible for voting")
# else:
#     print(f"{name}! your are not eligible for voting")
n = int(input("Enter a number: "))

# for i in range(n, (n*10)+1, n):
#     print(i)
# sum = 0
# fact = 1
# for i in range(1, n+1):
#     sum += i
#     fact *= i
#     print(f"the factorial of {n} is: {fact}")

# print(f"the sum of first {n} natural numbers is: {sum}")
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         even += i
# else:
#     odd += i
# print(even)
# print(odd)
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print(f"{n} is a prime number")

print(f"the number of factors of {n} is: {count}")

# reverse a string without using in build functions
name = input("Enter a string:")

reversed_name = ""
for i in range(len(name)-1, -1, -1):
    reversed_name += name[i]

print(f"The reversed string is: {reversed_name}")
# check if a string is palindrome or not
string = input("Enter a string: ")
reversed_string = ""
for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]
if string == reversed_string:
    print(f"{string} is a palindrome")
else:
    print(f"{reversed_string} is not a palindrome")
