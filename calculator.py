a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))

print("\nWhat you want to do: ")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

c= int(input("Enter the choice:-"))

if c==1:
    print("The result is ",a+b)
elif c==2:
    print("The result is ",a-b)
elif c==3:
    print("The result is ",a*b)
elif  c==4:
    print("The result is ",a/b)