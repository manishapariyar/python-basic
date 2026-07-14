original = int(input("Enter a number: "))
a = original
reverse = 0
while a > 0:
    reminder = a % 10
    reverse = reverse * 10 + a % 10
    a = a//10

if reverse == original:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
