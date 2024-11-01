#number greater than 50 and is even

num=int(input("Enter a number"))

if num>50:
    print(num," is greater than 50")
    if num%2==0:
        print("And the nuber is even")
    else:
        print("And the number is odd")
else:
    print(num," is less than 50")